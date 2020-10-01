from flask import Flask
from flask_login import LoginManager

from .controllers import controllers, users
from .config import Config

from app.model.user import User

#Instanciar el Login manager
login_manager = LoginManager()

#El user_loader acccedera al diccionario donde se almacenan los usuarios consesión activa
@login_manager.user_loader
def loader(user_id):

    try:
        return users[int(user_id)]

    except KeyError:
        return None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(controllers)

    login_manager.login_view = '/'
    login_manager.init_app(app)

    return app