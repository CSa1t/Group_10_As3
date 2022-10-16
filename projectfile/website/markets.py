from flask import Blueprint, render_template, request, redirect, url_for
from .models import Market
from .forms import MarketForm
from . import db
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
bp = Blueprint('market', __name__, url_prefix='/markets')

@bp.route('/create', methods = ['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  form = MarketForm()
  if form.validate_on_submit():
    market = Market(name=form.name.data,
    description= form.description.data,
    image=form.image.data,
    currency=form.currency.data)
    # add the object to the db session
    db.session.add(market)
    # commit to the database
    db.session.commit()
    print('Successfully created new market', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('market.create'))
  return render_template('markets/create.html', form=form)
