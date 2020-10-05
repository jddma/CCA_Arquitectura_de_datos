import logging

import sys

import os

import pymysql.cursors


class Database():

    def _open_connection(self):
        try:


            #Conactar a la base de datos obteniendo las credenciales de las variables de entorno
            self._connection = pymysql.connect(
                host=os.environ["MY_HOST"],
                user=os.environ["MY_USER"],
                password=os.environ["MY_PASSWORD"],
                db="cca",
                cursorclass=pymysql.cursors.DictCursor
            )

        #Excepción en caso de no poder obtener el valor de las variables de entorno
        except KeyError:
            logging.fatal("Error al obtener las credenciales de las variables de entorno")
            sys.exit()

        except Exception as ex:
            logging.fatal("Error al obtener las credenciales de las variables de entorno")
            sys.exit()

    #Para cerrar la conexión a la base de datos
    def _close_connection(self):
        try:
            self._connection.close()
        except:
            logging.fatal("Error al conectar con la base de datos")