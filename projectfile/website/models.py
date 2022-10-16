from . import db
from datetime import datetime


class Market(db.Model):
    __tablename__ = 'Markets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    comments = db.relationship('Comment', backref='markets')

    
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)
