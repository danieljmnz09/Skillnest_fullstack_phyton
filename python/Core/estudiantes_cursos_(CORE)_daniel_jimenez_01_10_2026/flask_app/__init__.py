import os
from flask import Flask
from flask_bcrypt import Bcrypt # Importar Bcrypt
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Inicializar Bcrypt con la app de Flask
bcrypt = Bcrypt(app)
