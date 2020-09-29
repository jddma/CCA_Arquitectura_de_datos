from flask_login import UserMixin, login_user

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):

    def __init__(self, id, name, email, id_rank):
        self.id = id
        self.__name = name
        self.__email = email
        self.__id_rank = id_rank

    def login(self, password):

        #Validación del usuario
        login_user(self)
        return True
