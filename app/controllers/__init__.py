from flask import Blueprint


controllers = Blueprint("controllers", __name__, url_prefix="/controllers")

from . import paths