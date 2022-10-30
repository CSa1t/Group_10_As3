from . import db
from datetime import datetime
from flask_login import UserMixin


class Market(db.Model):
    __tablename__ = 'markets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    #comments = db.relationship('Comment', backref='markets')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name, self.id)

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), index = True, unique = True, nullable = False)
    email_id = db.Column(db.String(100), index = True, nullable = False)
    password_hash = db.Column(db.String(255), nullable = False)
    usertype = db.Column(db.String(20), nullable = False, default = 'guest')

    #comments = db.relationship('Comment', backref='users')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.user_name, self.id)


