# __init__ will make the website directory a python package

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'cjsd skjcnsd ksjcnsdkjcn' # private key for the app

    return app