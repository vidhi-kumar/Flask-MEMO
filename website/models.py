# schema for our database
from . import db # from . means: from present directory
from flask_login import UserMixin # some functions to help with user
from sqlalchemy.sql import func # func can return time

# this is how we create class for objects of database
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foreign key,'u' us not capital
                                                  # for foreign key
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    notes = db.relationship('Note') # here we make the relationship, capital here




# class Reminder(db.Model)
# you can have more features!!
    