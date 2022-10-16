from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo

#Create new event
class MarketForm(FlaskForm):
  name = StringField('Event Name *', validators=[InputRequired()])
  type = SelectField(u'Event Type *', choices=[('Fruits & Vegetables'), ('Meats'), ('Wine & Drinks'), ('Dairy')])
  status = SelectField(u'Status *', choices=[('Open'), ('Unpublished'), ('Sold-Out'), ('Cancelled')])
  location = TextAreaField('Location *', validators=[InputRequired()])
  venue = TextAreaField('Venue', validators=[InputRequired()])
  description = TextAreaField('Description *', validators=[InputRequired()])
  image = StringField('Event Image *', validators=[InputRequired()])
  currency = StringField('Ticket Currency', validators=[InputRequired()])
  submit = SubmitField("Create") 
