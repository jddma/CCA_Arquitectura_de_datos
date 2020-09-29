from app import create_app

from flask import render_template

if __name__ == "__main__":

    #Intancia la aplicación de flask
    app = create_app()

    #Definir las rutas de las vistas
    @app.route('/')
    def index():
        return render_template("index.html")

    app.run(debug=True)