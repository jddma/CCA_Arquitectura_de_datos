from . import controllers

from app.model.user import User

from flask_login import login_required, current_user


@controllers.route("/login")
def login():
   userModel = User(1, "Juan", "jdmelo002@gmail.com", 1)
   if userModel.login("password"):
       return "Usuario verificado correctamente correctamente"

@controllers.route("/logout")
@login_required
def logout():
    a = current_user.__name
    return "No estamos listos again"