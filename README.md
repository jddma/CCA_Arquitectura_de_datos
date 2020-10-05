# CCA_arquitectura_de_datos
Aplicativo web para la administración de un centro de contacto responsable de realizar las convocatorias a diferentes campañas de donación

## Dependencias
* Python 3.7+
* virtualenv
* Flask
* Flask-Login
* MYSQL
* PyMySQL
* cryptography
* validate-email

## Descarga e instalación
* Instalar [_python 3.7+_](https://www.python.org/)
* Instalar [_virtualenv_](https://pypi.org/project/virtualenv/)
* Ejecutar en bash: 
    ```bash
        $ git clone https://github.com/jddma/CCA_arquitectura_de_datos.git
        $ cd CCA_arquitectura_de_datos/
        $ virtualenv venv --python=pyhon3.7

    
        # --- GNU lINUX / macOS ---
        $ source venv/bin/activate
  
        # --- Windows ---
        $ .\venv\scripts\activate
  
  
        (venv)$ pip3 install -r requirements.txt
    ```
## Configuración
* Crear las siguientes variables de entorno en el sistema con la información de la base de datos
    * MY_HOST="host"
    * MY_USER="user"
    * MY_PASSWORD="password"
    
## Licencia

CCA_arquitectura_de_datos esta bajo la licencia GNU General Public License v3.0, Leer el archivo [LICENSE](https://github.com/jddma/CCA_arquitectura_de_datos/blob/master/LICENSE) para mas información.