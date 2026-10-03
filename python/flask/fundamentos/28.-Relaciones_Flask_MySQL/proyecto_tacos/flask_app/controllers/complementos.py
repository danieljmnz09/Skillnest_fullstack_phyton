from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.complemento import Complemento
from flask_app.models.taco import Taco

@app.route("/complementos")
def index_complementos():
    todos_complementos = Complemento.get_all()
    todos_tacos = Taco.get_all()
    return render_template(
        "complementos.html",
        complementos=todos_complementos,
        tacos=todos_tacos
    )

@app.route("/complementos/crear", methods=["POST"])
def crear_complemento():
    datos = {
        "nombre_complemento": request.form["nombre_complemento"].strip()
    }
    Complemento.save(datos)
    return redirect(url_for("index_complementos"))

@app.route("/complementos/asociar", methods=["POST"])
def asociar_complemento():
    datos = {
        "complemento_id": request.form["complemento_id"],
        "taco_id": request.form["taco_id"]
    }
    Complemento.asociar_taco(datos)
    return redirect(url_for("index_complementos"))

@app.route("/complementos/<int:id>")
def ver_complemento(id):
    datos = {"id": id}
    complemento_obj = Complemento.get_complementos_y_tacos(datos)

    if complemento_obj is None:
        return "Complemento no encontrado", 404

    return render_template("complemento_detalle.html", complemento=complemento_obj)