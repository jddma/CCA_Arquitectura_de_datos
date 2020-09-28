from flask_login import UserMixin, login_user

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):

    def __init__(self, id, name, email, password, id_rank):
        self.id = id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__id_rank = id_rank

    def login(self):

        #Validación del usuario
        del self.__password
        login_user(self)
        return True
