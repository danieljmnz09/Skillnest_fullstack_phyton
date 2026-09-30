import os
from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# Leemos el archivo .env para usar las claves ocultas
load_dotenv()

app = Flask(__name__)
# Clave para manejar las sesiones
app.secret_key = os.getenv("SECRET_KEY")

# Herramienta para encriptar contraseñas
bcrypt = Bcrypt(app)