from . import controllers, users

from app.model.user import User

from flask_login import login_required, current_user



@controllers.route("/login")
def login():
    id = 1
    userModel = User(id, "Juan", "jdmelo002@gmail.com", 1)
    if userModel.login("password"):
        users[id] = userModel
        return "Usuario verificado correctamente correctamente"

@controllers.route("/logout")
@login_required
def logout():
    a = current_user.name
    return "No estamos listos again"