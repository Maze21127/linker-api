from enum import unique

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})


class Url(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255), unique=True)
    real_link = db.Column(db.String(4096))
    uses = db.Column(db.Integer, default=0)

    group_id = db.Column(db.BigInteger, db.ForeignKey("groups.id"))

    def __init__(self, link: str, real_link: str, group_id: int | None, uses: int = 0):
        self.link = link
        self.real_link = real_link
        self.group_id = group_id
        self.uses = uses

    def json(self):
        return {
            "tg_od": self.tg_id,
            "link": self.link,
            "real_link": self.real_link,
            "uses": self.uses,
            "group_id": self.group_id
        }


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    tg_id = db.Column(db.BigInteger)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, tg_id: int, name: str):
        self.tg_id = tg_id
        self.name = name

    def json(self):
        return {
            "tg_id": self.tg_id,
            "name": self.name,
        }
