from flask import Blueprint #Represents a blueprint, a collection of routes 
        # and other app-related functions that can be registered on a real application later.

auth = Blueprint('auth', __name__)

@auth.route('/login') # below runs the function for this route
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign up</p>"