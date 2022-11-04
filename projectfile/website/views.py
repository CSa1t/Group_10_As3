from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import MarketForm, RegisterForm, LoginForm
from . import db
from .models import User, Create
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

