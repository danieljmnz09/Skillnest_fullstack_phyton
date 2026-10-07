from flask import Flask

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos la clave secreta para cifrar sesiones y mensajes flash
app.secret_key = "clave_secreta_super_segura"