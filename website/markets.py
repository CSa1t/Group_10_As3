from flask import Blueprint, render_template, request, redirect, url_for
from .models import Create
from .forms import MarketForm
from . import db
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
bp = Blueprint('market', __name__, url_prefix='/markets')

@bp.route('/<id>')
def show(id):
    market = Create.query.filter_by(id=id).first()
    # create the comment form
    return render_template('markets/show.html', market=market)

@bp.route('/create', methods = ['GET', 'POST'])
def create():
  form = MarketForm()
  
  print("form created")
  if form.validate_on_submit() == False:
    print("Form was filled wrong")
    print(form.name.data, form.type.data, form.status.data, form.location.data, form.venue.data, form.date.data, form.image.data, form.price.data, form.booking.data, form.description.data)
    
  if form.validate_on_submit():
    print("Form was filled right")

    market = Create(      
    name = form.name.data, 
    type = form.type.data, 
    status = form.status.data,
    location = form.location.data, 
    venue = form.venue.data, 
    date = form.date.data,
    image = form.image.data, 
    price = form.price.data, 
    booking = form.booking.data,
    description = form.description.data)

    # add the object to the db session
    db.session.add(market)
    # commit to the database
    db.session.commit()
    print('Successfully created new market', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('market.create'))
  print("end of form")
  return render_template('markets/create.html', form=form)

