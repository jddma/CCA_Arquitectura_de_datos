from . import controllers, users

from app.model.user import User

from flask import request, make_response, redirect, url_for

from flask_login import login_required, current_user

import json


@controllers.route("/login", methods=['POST'])
def login():

    #Validar que la solicitud se haga correctamente
    try:

        #Convertir el cuerpo de la respuesta en formato JSON que contiene las credenciales
        credentials = json.loads(request.data)

        #Instanciar el objeto User
        userModel = User(credentials['email'], credentials['password'])

        #Valida que el inicio de sesión sea correcto
        if userModel.login():
            users[userModel.id] = userModel
            response = make_response('Succes')
            response.headers['Content-Type'] = 'text/plain'
            return response

        else:
            response = make_response('Credentials error')
            response.headers['Content-Type'] = 'text/plain'
            return response

    except:
        response = make_response('error')
        response.status_code = 400
        response.headers['Content-Type'] = 'text/plain'
        return response


@controllers.route("/logout")
@login_required
def logout():
    current_user.logout()
    return redirect(url_for('index'))