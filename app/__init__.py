from flask import Flask

from .controllers import controllers
from .config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(controllers)

    app.config.from_object(Config)


    return app