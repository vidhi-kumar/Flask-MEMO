# here we have the pages of our website
from flask import Blueprint #Represents a blueprint, a collection of routes 
        # and other app-related functions that can be registered on a real application later.
from flask import render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') # below runs the function for this route
@login_required #cant go home without login
def home():
    return render_template("home.html", user=current_user) # this will render home.html
                                       # ^we can refer current user in our template                     
# we need to register these blueprints in init.py
