from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    address = db.Column(db.String(100))
    creation_date = db.Column(db.Date)


class Ticket(UserMixin, db.Model):
    __tablename__ = "ticket"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))
    type = db.Column(db.String(100))
    # Todo: check Boolean
    is_active = db.Column(db.Boolean)
    client_id = db.Column(db.String(100))
    creation_date = db.Column(db.Date)
