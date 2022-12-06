from flask import Flask

from app.services import utils
from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.globals.update(get_item=utils.get_item)

from app import views
