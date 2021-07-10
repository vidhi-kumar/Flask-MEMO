# __init__ will make the website directory a python package

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cjsd skjcnsd ksjcnsdkjcn' # private key for the app

    # importing views
    from .views import views
    from .auth import auth

    # registering the views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app