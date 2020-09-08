from flask import Flask

from .controllers import controllers

def create_app():
    app = Flask(__name__)
    app.register_blueprint(controllers)

    return app