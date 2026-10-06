from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.pedido import Pedido

@app.route("/")
def index():
    return redirect("/arepas")

# Pantalla Dashboard: /arepas
@app.route("/arepas")
def arepas():
    todos_pedidos = Pedido.get_all()
    return render_template("pedidos.html", pedidos=todos_pedidos)

# Pantalla Formulario: /pedido
@app.route("/pedido")
def nuevo_pedido():
    return render_template("nuevo_pedido.html")

# Procesar creación de pedido
@app.route("/pedidos/crear", methods=["POST"])
def crear_pedido():
    if not Pedido.validar_pedido(request.form):
        return redirect("/pedido")

    datos = {
        "nombre": request.form["nombre"],
        "cantidad": request.form["cantidad"],
        "relleno": request.form["relleno"]
    }
    Pedido.save(datos)
    return redirect("/arepas")