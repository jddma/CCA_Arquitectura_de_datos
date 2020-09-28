from app import create_app

from flask import render_template
from flask_login import LoginManager

if __name__ == "__main__":

    app = create_app()
    login_manager = LoginManager(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    app.run(debug=True)