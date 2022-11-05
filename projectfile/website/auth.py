from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm, RegisterForm, MarketForm
from .models import User, Create
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from . import db

#create a blueprint
bp = Blueprint('auth', __name__ )

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Register form submitted')

        uname = form.user_name.data
        pwd = form.password.data
        email = form.email_id.data

        pwd_hash = generate_password_hash(pwd)

        new_user = User(user_name = uname, password_hash = pwd_hash, email_id = email)
        db.session.add(new_user)
        db.session.commit()
        flash("Registered user successfully")
        return redirect(url_for('auth.register'))

    return render_template('forms.html', form = form, heading = 'Register')

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if(form.validate_on_submit()):
        name = form.user_name.data
        password = form.password.data
        u1 = User.query.filter_by(user_name = name).first()

        if u1 is None:
            error = 'Incorrect user name'
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect Password'
        if error is None:
            login_user(u1)
            return redirect(url_for('main.booking'))
        else:
            print(error)
            flash(error)

    return render_template('forms.html', form = form, heading = 'login')

@bp.route('/logout')
def logout():
    logout_user()
    return 'Sucessfully logged user out'