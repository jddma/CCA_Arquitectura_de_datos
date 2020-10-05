from flask import Blueprint

from flask_login import current_user

users = {}
controllers = Blueprint("controllers", __name__, url_prefix="/controllers")

from . import paths

def get_context():
    context_dict = current_user.__dict__
    del context_dict["_connection"]
    return context_dict