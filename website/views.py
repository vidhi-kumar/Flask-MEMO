# here we have the pages of our website
from flask import Blueprint #Represents a blueprint, a collection of routes 
        # and other app-related functions that can be registered on a real application later.
from flask import render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Note
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) # below runs the function for this route
@login_required #cant go home without login
def home():
    if request.method == "POST":
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note empty', category="error")    
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category="success")

    return render_template("home.html", user=current_user) # this will render home.html
                                       # ^we can refer current user in our template                     
# we need to register these blueprints in init.py
