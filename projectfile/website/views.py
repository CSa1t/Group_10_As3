from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import MarketForm, RegisterForm, LoginForm
from . import db
from .models import User, Market
from flask_login import login_required, current_user

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')


@mainbp.route('/eventdetails')
def eventdetails():
    return render_template('markets/eventdetails.html')

@mainbp.route('/booking')
def booking():
    return render_template('markets/booking.html')

@mainbp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():

    if current_user.usertype != 'admin':
        flash("Need administator login")
        return redirect(url_for('auth.login'))

    print('In create booking')
    form = MarketForm

    if form.validate_on_submit():
        new_booking = Market(name = form.name.data, description = form.description.data, image = form.image.data, currency = form.currency.data)

        db.session.add(new_booking)
        db.session.commit()
        return redirect(url_for('main.add_market'))
    
    return render_template('markets/create.html', form = form)

