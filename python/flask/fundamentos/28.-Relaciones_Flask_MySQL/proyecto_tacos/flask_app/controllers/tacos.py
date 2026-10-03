from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.taco import Taco
from flask_app.models.restaurante import Restaurante

@app.route("/")
def index():
    todos_restaurantes = Restaurante.get_all()
    return render_template("index.html", todos_restaurantes=todos_restaurantes)

@app.route("/crear", methods=["POST"])
def crear():
    datos = {
        "tortilla": request.form["tortilla"].strip(),
        "guiso": request.form["guiso"].strip(),
        "salsa": request.form["salsa"].strip(),
        "restaurante_id": request.form["restaurante_id"]
    }
    Taco.save(datos)
    return redirect(url_for("tacos"))

@app.route("/tacos")
def tacos():
    todos_los_tacos = Taco.get_all()
    return render_template("index.html", tacos=todos_los_tacos)

@app.route("/restaurantes")
def restaurantes():
    todos_restaurantes = Restaurante.get_all()
    return render_template("restaurantes.html", restaurantes=todos_restaurantes)

@app.route("/restaurantes/<int:id>")
def restaurante(id):
    datos = {"id": id}
    restaurante_obj = Restaurante.get_restaurante_y_tacos(datos)
    if restaurante_obj is None:
        return "Restaurante no encontrado", 404
    return render_template("restaurante.html", restaurante=restaurante_obj)