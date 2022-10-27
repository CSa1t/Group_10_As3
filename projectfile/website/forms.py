from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, DateField, FileField, DecimalField, IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange

#Create new event
class MarketForm(FlaskForm):
  name = StringField('Event Name', validators=[InputRequired()])
  type = SelectField(u'Event Type', choices=[('Fruits & Vegetables'), ('Meats'), ('Wine & Drinks'), ('Dairy')])
  status = SelectField(u'Status', choices=[('Open'), ('Unpublished'), ('Sold-Out'), ('Cancelled')])
  location = TextAreaField('Location', validators=[InputRequired()])
  venue = TextAreaField('Venue', validators=[InputRequired()])
  date = DateField('Event Date', validators=[InputRequired()])
  image = FileField('Event Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
  price = IntegerField('Ticket Price', validators=[NumberRange(min=0, max=100)] )
  booking = IntegerField('Amount of Tickets', validators=[NumberRange(min=0, max=10000)] )
  description = TextAreaField('Description', validators=[InputRequired()])
  submit = SubmitField("Create")
