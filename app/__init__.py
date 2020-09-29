from flask import Flask
from flask_login import LoginManager

from .controllers import controllers
from .config import Config

from app.model.user import User

login_manager = LoginManager()

@login_manager.user_loader
def loader(user_id):

    #consulta a la base de datos
    return User(1, "Juan Diego", "correo@dominio", 1)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(controllers)


    login_manager.login_view = '/'
    login_manager.init_app(app)

    return app