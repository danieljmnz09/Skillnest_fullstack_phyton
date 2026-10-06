import os
from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)
# Leemos la clave desde la variable de entorno o usamos una de respaldo por seguridad
app.secret_key = os.environ.get("SECRET_KEY", "clave_de_respaldo_segura")

bcrypt = Bcrypt(app)