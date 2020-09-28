from . import controllers

from app.model.user import User


@controllers.route("/login")
def login():
   userModel = User(1, "Juan", "jdmelo002@gmail.com", "1234", 1)
   if userModel.login():
       return "Usuario verificado correctamente correctamente"

@controllers.route("/logout")
def logout():
    return "No estamos listos again"