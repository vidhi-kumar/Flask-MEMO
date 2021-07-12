from flask import Blueprint #Represents a blueprint, a collection of routes 
        # and other app-related functions that can be registered on a real application later.

from flask import render_template, request
from flask import flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash #for hashing passw
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # below runs the function for this route
# methods is added so that post can work, without that only get works
def login():
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # checking if that email exists or not
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                #login procedure
                login_user(user, remember=True) # literally remembers user is loggedin
                                #until user deletes cookies or restart flask web server
                return redirect(url_for('views.home')) # go to home after login
                
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')


    return render_template("login.html", user=current_user)
                                        #^you know it                

@auth.route('/logout') # anything starting with @ is a decorator
@login_required # so that logout only works for 
def logout():
    logout_user()
    return redirect(url_for('auth.login')) #go to login

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # taking data only in post method
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # first we check if same email is not present in the database already
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        # conditions for data entered(messege flashing)
        elif len(email) < 5:
            flash('Email must be greater than 4 letters', category='error')
        elif len(first_name) < 1:
            flash('First name cannot be empty', category='error')
        elif len(last_name) < 1:
            flash('Last name cannot be empty', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error') # escape char used
        elif len(password1) < 5:
            flash('Password must contain atleast 5 characters', category='error')
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"))
            #sha56 is a hashing algo
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True) #direct login after signup
            flash('Account Created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)