from flask import Blueprint #Represents a blueprint, a collection of routes 
        # and other app-related functions that can be registered on a real application later.

from flask import render_template, request
from flask import flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # below runs the function for this route
# methods is added so that post can work, without that only get works
def login():
    # data = request.form
    # print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # taking data only in post method
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # conditions for data entered(messege flashing)
        if len(email) < 5:
            flash('Email must be greater than 4 letters', category='error')
        elif len(firstName) < 1:
            flash('First name cannot be empty', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error') # escape char used
        elif len(password1) < 5:
            flash('Password must contain atleast 5 characters', category='error')
        else:
            # add user to database
            flash('Account Created', category='success')

    return render_template("sign_up.html")