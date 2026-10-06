from flask import Flask

app = Flask(__name__)
app.secret_key = "clave_secreta_pedidos_arepas"
