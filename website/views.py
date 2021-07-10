# here we have the pages of our website
from flask import Blueprint #Represents a blueprint, a collection of routes 
        # and other app-related functions that can be registered on a real application later.

views = Blueprint('views', __name__)

@views.route('/') # below runs the function for this route
def home():
    return "<h1>Testing</h1>"
# we need to register these blueprints in init.py
