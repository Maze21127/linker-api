from app.models import Group, db, Url


def create_group(group_name: str,  owner_id: int):
    try:
        group = Group(name=group_name, tg_id=owner_id)
        db.session.add(group)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False


def get_page_for_group(group: Group):
    base = f"""
<h1>Group.id {group.id}</h1>    
<h1>Group.name {group.name}</h1>
<h1>Group.tg_id {group.tg_id}</h1>
"""
    pages = Url.query.filter_by(group_id=group.id).order_by(Url.id)
    for page in pages:
        base += f'<a href="{page.real_link}">{page.link}</a>\n'
    return base


def get_pages_for_group(group: Group):
    return Url.query.filter_by(group_id=group.id).all()
