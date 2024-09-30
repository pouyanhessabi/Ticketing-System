from datetime import date

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required

from .model import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(name=name).first()

    if not user:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    if not name:
        flash('Name field can not be empty')
        return redirect(url_for('auth.signup'))
    password = request.form.get('password')
    phone = request.form.get('phone')
    address = request.form.get('address')
    user = User.query.filter_by(name=name).first()

    if user:
        flash('Name already exists')
        return redirect(url_for('auth.signup'))

    new_user = User()
    new_user.name = name
    new_user.password = password
    new_user.phone = phone
    new_user.address = address
    new_user.creation_date = date.today()
    # add the new user to the database
    from . import db
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
