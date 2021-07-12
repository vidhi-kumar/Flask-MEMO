# __init__ will make the website directory a python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # for database

# defining a new database
db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cjsd skjcnsd ksjcnsdkjcn' # private key for the app
    # time to tell app about our database and its location
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # now we pass app to database
    db.init_app(app)
    

    # importing views
    from .views import views
    from .auth import auth

    # registering the views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app