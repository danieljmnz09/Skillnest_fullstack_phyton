🧩 Arquitectura de una aplicación Flask con MySQL
Guía de comprensión: cómo organizar un proyecto Flask profesional utilizando Blueprints, Controllers, Models, MySQL, variables de entorno y request.


🎯 Objetivo
Aprender a comprender la estructura de una aplicación Flask que ha crecido más allá de un solo archivo.

En proyectos pequeños podemos tener:

app.py

con todas las rutas y lógica.

Pero cuando la aplicación crece aparecen muchas responsabilidades:

usuarios;
misiones;
autenticación;
base de datos;
formularios;
archivos;
plantillas;
lógica de negocio.

En ese momento necesitamos separar el proyecto.

La idea central de esta arquitectura es:

Cada archivo tiene una responsabilidad.


1. 🧠 ¿Por qué separar los archivos?
Imagina que todo nuestro proyecto estuviera dentro de:

app.py

y tuviéramos:

# Usuarios

@app.route("/usuarios")

def usuarios():

    ...


# Misiones

@app.route("/misiones")

def misiones():

    ...


# Login

@app.route("/login")

def login():

    ...


# Consultas SQL

...


# Conexión MySQL

...


# Validaciones

...


# Procesamiento

Al principio puede funcionar.

El problema aparece cuando la aplicación empieza a crecer.

app.py

│

├── Usuarios

├── Misiones

├── Login

├── Registro

├── SQL

├── MySQL

├── Validaciones

├── Formularios

└── ...

El archivo termina siendo difícil de:

leer;
modificar;
depurar;
mantener;
reutilizar.

Por eso dividimos el proyecto.


2. 🏗️ La idea de separación de responsabilidades
Una arquitectura organizada puede verse así:

FLASK

│

├── Controllers

│      ↓

│   reciben solicitudes

│

├── Models

│      ↓

│   trabajan con los datos

│

├── Database

│      ↓

│   conecta con MySQL

│

├── Templates

│      ↓

│   muestran información

│

└── Static

       ↓

    CSS / JS / imágenes

Podemos imaginarlo como una empresa:

Controllers

    ↓

Recepción

Models

    ↓

Administración de datos

Database

    ↓

Conexión con sistemas externos

Templates

    ↓

Presentación al cliente


3. 📁 Estructura del proyecto
Una estructura habitual podría ser:

flask_app/

│

├── __init__.py

├── app.py

├── .env

├── requirements.txt

│

├── controllers/

│   ├── controlador_usuarios.py

│   └── controlador_misiones.py

│

├── models/

│   ├── usuario.py

│   └── mision.py

│

├── templates/

│

└── static/

    ├── css/

    ├── js/

    └── img/

Cada carpeta tiene una función específica.


4. 🐍 __init__.py
Comencemos por el archivo que crea la aplicación Flask.

flask_app/

└── __init__.py
Código
from flask import Flask

# Creamos una única instancia de Flask.

app = Flask(__name__)

# Clave necesaria para utilizar session.

#

# En producción debería almacenarse mediante

# una variable de entorno.

app.secret_key = "clave-de-desarrollo"


🔍 ¿Qué hace este archivo?
La línea:

app = Flask(__name__)

crea nuestra aplicación.

Podemos imaginarlo así:

__init__.py

      ↓

crea

      ↓

app

      ↓

aplicación Flask

Todos los demás componentes podrán trabajar con esa misma aplicación.


5. 📦 requirements.txt
Este archivo contiene las dependencias necesarias para ejecutar el proyecto.

Flask

PyMySQL

python-dotenv

Por ejemplo:

requirements.txt

puede contener:

Flask==3.1.2

PyMySQL==1.1.1

python-dotenv==1.1.1

Luego una persona que descargue el proyecto puede instalar todo mediante:

pip install -r requirements.txt


🧠 ¿Por qué existe este archivo?
Sin requirements.txt, otra persona tendría que averiguar:

¿Qué librerías necesita el proyecto?

Con él:

requirements.txt

       ↓

pip install -r requirements.txt

       ↓

dependencias instaladas


6. 🔐 .env
Las aplicaciones suelen necesitar información que no debería escribirse directamente en el código.

Por ejemplo:

MYSQL_HOST

MYSQL_USER

MYSQL_PASSWORD

MYSQL_DATABASE

Creamos:

.env

con:

# ==========================================

# CONFIGURACIÓN DE BASE DE DATOS

# ==========================================

MYSQL_HOST=localhost

MYSQL_USER=root

MYSQL_PASSWORD=TU_PASSWORD

MYSQL_DATABASE=voluntame_db

Importante: nunca publiques contraseñas reales en GitHub. El archivo .env normalmente debe incluirse en .gitignore.


7. 🚫 .gitignore
Agregamos:

.env

venv/

__pycache__/

*.pyc

Por ejemplo:

.gitignore

puede contener:

venv/

__pycache__/

*.pyc

.env

Así evitamos subir información sensible.


8. 📥 load_dotenv()
Para utilizar .env, instalamos:

python-dotenv

y luego:

from dotenv import load_dotenv

load_dotenv()

Esto carga las variables definidas en .env.

Podemos imaginarlo así:

.env

 ↓

load_dotenv()

 ↓

variables de entorno


9. 🧩 os.environ.get()
Una vez cargadas las variables:

import os

podemos obtenerlas:

host = os.environ.get("MYSQL_HOST")

o:

password = os.environ.get("MYSQL_PASSWORD")

Por ejemplo:

MYSQL_HOST=localhost

permite:

os.environ.get("MYSQL_HOST")

obtener:

localhost


10. 🐬 Conexión a MySQL
Ahora necesitamos una pieza que se encargue exclusivamente de hablar con MySQL.

Creamos:

mysqlconnection.py


🔌 mysqlconnection.py
import os

import pymysql.cursors

from dotenv import load_dotenv


# ==========================================================

# CARGAR VARIABLES DE ENTORNO

# ==========================================================

load_dotenv()


# ==========================================================

# CONEXIÓN MYSQL

# ==========================================================

class MySQLConnection:

    def __init__(self, db):

        self.connection = pymysql.connect(

            host=os.environ.get("MYSQL_HOST"),

            user=os.environ.get("MYSQL_USER"),

            password=os.environ.get("MYSQL_PASSWORD"),

            database=db,

            charset="utf8mb4",

            cursorclass=pymysql.cursors.DictCursor,

            autocommit=True

        )


    # ======================================================

    # EJECUTAR CONSULTAS

    # ======================================================

    def query_db(self, query, data=None):

        with self.connection.cursor() as cursor:

            try:

                print("Ejecutando consulta:")

                print(query)


                cursor.execute(query, data)


                # --------------------------------------------------

                # SELECT

                # --------------------------------------------------

                if query.strip().lower().startswith("select"):

                    return cursor.fetchall()


                # --------------------------------------------------

                # INSERT

                # --------------------------------------------------

                elif query.strip().lower().startswith("insert"):

                    return cursor.lastrowid


                # --------------------------------------------------

                # UPDATE / DELETE

                # --------------------------------------------------

                else:

                    return None


            except Exception as e:

                print("Error en la Base de Datos:")

                print(e)

                return False


            finally:

                self.connection.close()


# ==========================================================

# FUNCIÓN AUXILIAR

# ==========================================================

def connect_to_mysql(db):

    return MySQLConnection(db)


🧠 ¿Qué responsabilidad tiene este archivo?
Solamente la conexión y ejecución de consultas.

mysqlconnection.py

       │

       ├── conectar

       ├── ejecutar SQL

       ├── recuperar resultados

       └── cerrar conexión

El controlador no necesita saber todos estos detalles.

El modelo tampoco.

Simplemente pueden solicitar:

connect_to_mysql(...)


11. 📊 DictCursor
Tenemos:

cursorclass=pymysql.cursors.DictCursor

Esto hace que un SELECT pueda devolver:

[

    {

        "id": 1,

        "nombre": "Firulais",

        "tipo": "Perro"

    },

    {

        "id": 2,

        "nombre": "Michi",

        "tipo": "Gato"

    }

]

Es decir:

SELECT

 ↓

lista

 ↓

diccionarios

Esto resulta muy cómodo para trabajar posteriormente con objetos y Jinja2.


12. 🐕 Models
Ahora tenemos que representar nuestros datos.

Supongamos una tabla:

mascotas

crearemos:

models/

└── mascota.py


🐕 mascota.py
from mysqlconnection import connect_to_mysql


class Mascota:

    def __init__(self, data):

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.tipo = data["tipo"]

        self.color = data["color"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    @classmethod

    def get_all(cls):

        query = """

            SELECT *

            FROM mascotas;

        """


        resultados = connect_to_mysql(

            "voluntame_db"

        ).query_db(query)


        mascotas = []


        for mascota in resultados:

            mascotas.append(

                cls(mascota)

            )


        return mascotas


🧠 ¿Qué hace un Model?
El modelo representa y gestiona los datos.

En este caso:

Mascota

representa:

tabla mascotas

Por lo tanto:

MySQL

 ↓

mascotas

 ↓

Mascota

 ↓

objetos Python


13. 🔄 @classmethod
Observa:

@classmethod

def get_all(cls):

Esto permite llamar:

Mascota.get_all()

sin crear primero una mascota.

Tiene sentido porque:

get_all()

consulta toda la colección de mascotas.


14. 🔎 Consultar por ID
Podríamos agregar:

@classmethod

def get_by_id(cls, data):

    query = """

        SELECT *

        FROM mascotas

        WHERE id = %(id)s;

    """

    resultado = connect_to_mysql(

        "voluntame_db"

    ).query_db(query, data)

    if not resultado:

        return None

    return cls(resultado[0])

Entonces:

data = {

    "id": 5

}

y:

Mascota.get_by_id(data)

buscará:

mascota #5


15. 📦 ¿Qué es data?
data suele ser un diccionario que contiene valores que necesita una consulta.

Por ejemplo:

data = {

    "id": 5

}

y una consulta:

SELECT *

FROM mascotas

WHERE id = %(id)s;

La clave:

id

se relaciona con:

%(id)s


16. 🗑️ Mision.eliminar(data)
Una llamada como:

Mision.eliminar(data)

significa:

Ejecutar el método eliminar() de la clase Mision.

Por ejemplo:

data = {

    "id_mision": id_mision

}

Mision.eliminar(data)

Si:

id_mision = 25

entonces:

data = {

    "id_mision": 25

}

El modelo podría ejecutar:

DELETE

FROM misiones

WHERE id_mision = %(id_mision)s;


17. 🔗 Mision.obtener_por_id_con_relaciones(data)
Esta llamada:

mision = Mision.obtener_por_id_con_relaciones(data)

significa:

Obtener una misión mediante su identificador incluyendo información relacionada.

Por ejemplo:

Misión

│

├── organización

├── categoría

├── responsable

└── participantes

Esto normalmente implica una consulta SQL con JOIN o varias consultas coordinadas.


18. 🧭 Controllers
Ahora llegamos a una de las piezas más importantes.

Los Controllers reciben las solicitudes HTTP y deciden qué debe ocurrir.

Por ejemplo:

controllers/

│

├── controlador_usuarios.py

└── controlador_misiones.py

Podemos imaginar:

Navegador

    ↓

Controller

    ↓

Model

    ↓

MySQL


19. 🧩 Blueprint
Antes de definir un Controller, aparece:

Blueprint

Un Blueprint permite agrupar rutas relacionadas.

Por ejemplo:

usuarios

 ↓

usuarios_bp

misiones

 ↓

misiones_bp


20. Crear un Blueprint
En:

controlador_misiones.py

podemos tener:

from flask import Blueprint

misiones_bp = Blueprint(

    "misiones",

    __name__

)

Esta línea crea un Blueprint llamado:

misiones


🧠 ¿Qué significa __name__?
__name__ es una variable especial de Python que identifica el módulo actual.

No necesitamos memorizar su funcionamiento interno para utilizar Blueprint.

En términos sencillos:

Blueprint("misiones", __name__)

significa:

Crear un grupo de rutas llamado misiones dentro de este módulo.


21. Rutas dentro del Blueprint
Podemos definir:

@misiones_bp.route("/dashboard")

def dashboard():

    return "Dashboard de misiones"

Ahora esta ruta pertenece al Blueprint:

misiones_bp

y no directamente a:

app


22. @app.route() vs @misiones_bp.route()
Sin Blueprint:

@app.route("/dashboard")

def dashboard():

Con Blueprint:

@misiones_bp.route("/dashboard")

def dashboard():

La diferencia está en quién administra la ruta.

@app.route

    ↓

aplicación principal

@misiones_bp.route

    ↓

Blueprint


23. Registrar un Blueprint
Crear el Blueprint no es suficiente.

Hay que registrarlo.

En nuestro archivo principal:

from flask_app import app

from flask_app.controllers.controlador_usuarios import usuarios_bp

from flask_app.controllers.controlador_misiones import misiones_bp


app.register_blueprint(usuarios_bp)

app.register_blueprint(misiones_bp)


🧠 ¿Qué hace register_blueprint()?
Esta línea:

app.register_blueprint(misiones_bp)

puede leerse como:

"Agrega todas las rutas de misiones_bp a nuestra aplicación Flask."

Visualmente:

misiones_bp

│

├── /dashboard

├── /crear

├── /editar

└── /eliminar

       │

       ▼

register_blueprint()

       │

       ▼

      app


24. ¿Por qué usar Blueprint?
Supongamos que tenemos:

100 rutas

No queremos tener:

app.py

    ↓

100 rutas

Podemos dividirlas:

usuarios

    ↓

usuarios_bp

    ↓

20 rutas

misiones

    ↓

misiones_bp

    ↓

30 rutas

organizaciones

    ↓

organizaciones_bp

    ↓

25 rutas

auth

    ↓

auth_bp

    ↓

25 rutas

Así cada módulo queda organizado.


25. 📥 request
Ahora necesitamos entender cómo el servidor recibe información del navegador.

Flask proporciona:

request

request representa la solicitud HTTP actual.


26. request.form
Si tenemos:

<form method="POST">

    <input

        type="text"

        name="nombre"

    >

    <button type="submit">

        Guardar

    </button>

</form>

podemos recibir:

from flask import request

y:

nombre = request.form["nombre"]

Si el usuario escribió:

Dany

obtendremos:

Dany


27. request.args
Si tenemos:

/buscar?nombre=Dany

podemos obtener:

nombre = request.args.get("nombre")

Entonces:

URL

 ↓

request.args

 ↓

nombre


28. Diferencia entre request.form y request.args
Elemento
Uso
request.form
Datos enviados mediante formularios, normalmente POST
request.args
Parámetros incluidos en la URL, normalmente GET


Ejemplo POST:

request.form["nombre"]

Ejemplo GET:

request.args.get("nombre")


29. request.method
También podemos consultar el método HTTP:

request.method

Puede entregar:

GET

o:

POST

Por ejemplo:

if request.method == "POST":

    ...


30. Controller completo
Ahora podemos unir Blueprint + request + Model.

from flask import (

    Blueprint,

    render_template,

    request,

    redirect,

    url_for

)

from flask_app.models.mision import Mision


# ==========================================================

# BLUEPRINT

# ==========================================================

misiones_bp = Blueprint(

    "misiones",

    __name__

)


# ==========================================================

# DASHBOARD

# ==========================================================

@misiones_bp.route("/dashboard")

def dashboard():

    misiones = Mision.obtener_todas()

    return render_template(

        "misiones/dashboard.html",

        misiones=misiones

    )


# ==========================================================

# ELIMINAR MISIÓN

# ==========================================================

@misiones_bp.route(

    "/eliminar/<int:id_mision>",

    methods=["POST"]

)

def eliminar(id_mision):

    data = {

        "id_mision": id_mision

    }

    Mision.eliminar(data)

    return redirect(

        url_for("misiones.dashboard")

    )


🔍 Analizando el flujo
Cuando el usuario visita:

/misiones/dashboard

el recorrido puede ser:

Navegador

    ↓

Flask

    ↓

misiones_bp

    ↓

dashboard()

    ↓

Mision.obtener_todas()

    ↓

mysqlconnection.py

    ↓

MySQL

    ↓

datos

    ↓

Jinja2

    ↓

HTML

    ↓

Navegador


31. ¿Qué ocurre al eliminar?
Supongamos:

POST /eliminar/25

Flask recibe:

id_mision = 25

Luego:

data = {

    "id_mision": 25

}

Después:

Mision.eliminar(data)

El modelo puede ejecutar:

DELETE

FROM misiones

WHERE id_mision = %(id_mision)s;

Finalmente:

return redirect(

    url_for("misiones.dashboard")

)


32. url_for() con Blueprints
Aquí aparece una diferencia importante.

Sin Blueprint podemos tener:

url_for("index")

Pero si la función pertenece a un Blueprint llamado:

misiones

podemos utilizar:

url_for("misiones.dashboard")

La estructura es:

nombre_blueprint.nombre_funcion

Por ejemplo:

url_for("misiones.dashboard")

busca:

def dashboard():

dentro del Blueprint:

misiones


33. Flujo completo de una aplicación profesional
Ahora podemos unir todas las piezas.

                         NAVEGADOR

                              │

                              │ HTTP

                              ▼

                           FLASK

                              │

                 register_blueprint()

                              │

              ┌───────────────┴───────────────┐

              │                               │

              ▼                               ▼

        usuarios_bp                    misiones_bp

              │                               │

              ▼                               ▼

         Controller                       Controller

              │                               │

              │                               │

              └───────────────┬───────────────┘

                              ▼

                            Model

                              │

                              ▼

                     MySQLConnection

                              │

                              ▼

                           PyMySQL

                              │

                              ▼

                            MySQL

                              │

                              ▼

                             Datos

                              │

                              ▼

                          Jinja2

                              │

                              ▼

                            HTML

                              │

                              ▼

                         NAVEGADOR


34. 🧠 ¿Qué hace cada pieza?
__init__.py
Crea la aplicación Flask.


Blueprint
Agrupa rutas relacionadas.


Controller
Recibe solicitudes y coordina qué debe ocurrir.


request
Permite acceder a la información enviada por el navegador.


Model
Representa y consulta los datos.


MySQLConnection
Administra la conexión y ejecución de SQL.


.env
Contiene configuración sensible o específica del entorno.


requirements.txt
Define las dependencias Python del proyecto.


templates
Presentan la información al usuario.


35. 📚 Diccionario rápido
Elemento
Significado
Flask()
Crea la aplicación
Blueprint()
Crea un grupo de rutas
route()
Define una URL
register_blueprint()
Registra un Blueprint
request
Solicitud HTTP actual
request.form
Datos enviados por formulario
request.args
Parámetros enviados por URL
request.method
Método HTTP utilizado
session
Información mantenida entre solicitudes
render_template()
Renderiza HTML
redirect()
Envía al navegador a otra ruta
url_for()
Genera URLs de Flask
@classmethod
Permite ejecutar métodos desde la clase
data
Diccionario de parámetros
DictCursor
Devuelve registros SQL como diccionarios
fetchall()
Obtiene todos los registros
lastrowid
Obtiene el ID generado por INSERT
commit()
Confirma modificaciones
load_dotenv()
Carga variables desde .env
os.environ.get()
Obtiene una variable de entorno
requirements.txt
Dependencias
.env
Configuración sensible
__init__.py
Inicialización del paquete/aplicación



🎯 La idea más importante
No memorices la arquitectura como una colección de archivos independientes.

Piensa en responsabilidades.

¿Quién recibe la solicitud?

        ↓

    Controller

¿Quién contiene los datos?

        ↓

      Model

¿Quién habla con MySQL?

        ↓

MySQLConnection

¿Quién muestra la información?

        ↓

     Jinja2

¿Quién organiza las rutas?

        ↓

    Blueprint

¿Dónde están las credenciales?

        ↓

       .env

¿Dónde están las dependencias?

        ↓

requirements.txt


🏁 Resumen final
Una aplicación Flask grande puede organizarse así:

flask_app/

│

├── __init__.py

│       ↓

│   crea Flask

│

├── controllers/

│       ↓

│   reciben solicitudes

│

├── models/

│       ↓

│   trabajan con datos

│

├── mysqlconnection.py

│       ↓

│   conecta con MySQL

│

├── templates/

│       ↓

│   muestran HTML

│

├── static/

│       ↓

│   CSS / JS / imágenes

│

├── .env

│       ↓

│   configuración

│

└── requirements.txt

        ↓

    dependencias

El flujo fundamental es:

NAVEGADOR

    ↓

FLASK

    ↓

BLUEPRINT

    ↓

CONTROLLER

    ↓

MODEL

    ↓

MYSQLCONNECTION

    ↓

MYSQL

    ↓

MODEL

    ↓

CONTROLLER

    ↓

JINJA2

    ↓

HTML

    ↓

NAVEGADOR

Una vez entendido este flujo, conceptos como:

Mision.eliminar(data)

Mision.obtener_por_id_con_relaciones(data)

request.form

misiones_bp.route()

app.register_blueprint()

load_dotenv()

os.environ.get()

dejan de parecer instrucciones aisladas y empiezan a tener sentido dentro de una arquitectura completa.

