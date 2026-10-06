from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    return redirect("/usuarios")

@app.route("/usuarios")
def usuarios():
    relaciones = Usuario.get_todas_relaciones_seguidores()
    todos_usuarios = Usuario.get_all()
    return render_template(
        "usuarios.html",
        relaciones=relaciones,
        todos_usuarios=todos_usuarios
    )

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(datos)
    return redirect("/usuarios")

@app.route("/seguidores/crear", methods=["POST"])
def crear_seguidor():
    datos = {
        "usuario_id": request.form["usuario_id"],
        "seguidor_id": request.form["seguidor_id"]
    }
    Usuario.agregar_seguidor(datos)
    return redirect("/usuarios")