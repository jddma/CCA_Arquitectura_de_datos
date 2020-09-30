from .database import Database

from flask_login import UserMixin, login_user, logout_user

from validate_email import validate_email

from werkzeug.security import check_password_hash


class User(UserMixin, Database):

    def __init__(self, email, password):
        self.password = password
        self.email = email

    #Método para logear al usuarios retorna true si el login fue exitoso y false en caso contrario
    def login(self):

        #Validar que la información ingresada corresponsa a un email
        if validate_email(self.email):
            self._open_connection()

            #Query para consultar el usuario ingresado
            sql = "SELECT * FROM workers WHERE email = %s"
            with self._connection.cursor() as cursor:
                cursor.execute(sql, (self.email))
                result = cursor.fetchone()

                #Validar que el usaurio ingresado se encuentre registrado en la base de datos
                if result is None:
                    self._close_connection()
                    return False

                else:

                    #Validar que la contraseña ingresada corresponda a la registrada en al base de datos
                    if check_password_hash(result['password'], self.password):

                        #Elimina la contraseña del objeto para que no quede guardada en la sesión
                        del self.password

                        #Registra los otros datos de usuario obtenidos de la base de datos
                        self.id = result['WorkerID']
                        self.names = result['names']
                        self.lastnames = result['lastnames']
                        self.rank = result['Worker_rankID']

                        #Iniciar la sesión
                        login_user(self)

                        self._close_connection()
                        return True

                    else:
                        self._close_connection()
                        return False

        else:
            return False

    def logout(self):
        logout_user()