## python -m pipenv install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return " <h1>¡Oe conchatumare ooj</h1>!<p>Esto es un parrafo</p>"

@app.route("/exito")
def exito():
    return "¡Éxito!"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"¡Hola {nombre}!"

@app.route("/color/<nombre>/<color>")
def color_favorito(nombre, color):
    return f"Hola {nombre}, tu color favorito es {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):
    return f"¡Hola {nombre}!" * veces

@app.route("/despedida/<nombre>")
def despedida(nombre):
    return f"¡Chao nos vemos {nombre}!"

@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):
    return f"Hola {nombre} tienes {edad} años..."


if __name__ == "__main__":
    app.run(debug=True)