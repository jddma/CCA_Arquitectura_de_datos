from flask import Blueprint

users = {}
controllers = Blueprint("controllers", __name__, url_prefix="/controllers")

from . import paths