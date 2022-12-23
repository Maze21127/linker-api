from flask import Flask

from app.services import utils
from settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
from loguru import logger


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.jinja_env.globals.update(get_item=utils.get_item)

logger.add("logs/error.log", format="{time} {level} {message}", level="ERROR", rotation="01:00")
logger.add("logs/info.log", format="{time} {level} {message}", level="INFO", rotation="01:00")


from app import views
