from flask import Blueprint, render_template, request, redirect, url_for

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

@mainbp.route('/create')
def create():
    return render_template('markets/create.html')
