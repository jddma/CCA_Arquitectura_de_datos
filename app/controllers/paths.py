from . import controllers


@controllers.route("/login")
def login():
    return "NO estamos listos"

@controllers.route("/logout")
def logout():
    return "No estamos listos again"