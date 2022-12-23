
from flask import render_template, request, redirect
from app import app
from app.models import Url, Group
from app.services.group import create_group, get_pages_for_group
from app.services.link import create_link


@app.route('/', methods=['GET'])
def index():
    return "<h1>Working</h1>"


@app.route('/<link>', methods=['GET'])
def redirect_test(link):
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(ip)
    group = Group.query.filter_by(name=link).first()
    if group is None:
        source_link = Url.query.filter_by(link=link).first()
        if source_link is None:
            return "Такой страницы еще нет, но вы можете её купить здесь..."
        return redirect(source_link.real_link)
    return render_template('group_page.html', pages=get_pages_for_group(group), group_name=group.name)


@app.route('/api/v1/check_link/<redirect_link>', methods=['GET'])
def check_link(redirect_link):
    data = Url.query.filter_by(link=redirect_link).first()
    if data is not None:
        return {"status": "already exist",
                "code": 405}
    return {"status": "not exist",
            "code": 200}


@app.route('/api/v1/create_link/', methods=['POST'])
def create_link_page():
    form = request.form
    group_id = form['group'] if 'group' in form.keys() else None
    status = create_link(form['source'], form['link'], group_id)

    return {"status": "created",
            "code": 201} if status else \
        {"status": "already already_exists",
            "code": 401}


@app.route('/api/v1/create_group/', methods=['POST'])
def create_group_page():
    form = request.form
    create_group(form['group_name'], int(form['tg_id']))
    return {"status": "created",
            "code": 201}


@app.route('/api/v1/add_link/', methods=['POST'])
def add_link_page():
    form = request.form
    create_link(form['source'], form['link_name'], form['group_name'])
    return {"status": "created",
            "code": 201}
