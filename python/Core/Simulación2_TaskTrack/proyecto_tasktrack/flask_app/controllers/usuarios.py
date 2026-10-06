from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    if "usuario_id" in session:
        return redirect("/tareas")
    return render_template("login_registro.html")

@app.route("/registrarse", methods=["POST"])
def registrarse():
    if not Usuario.validar_registro(request.form):
        return redirect("/")

    usuario_id = Usuario.save(request.form)
    session["usuario_id"] = usuario_id
    session["nombre"] = request.form["nombre"]
    return redirect("/tareas")

@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.validar_login(request.form)
    if not usuario:
        return redirect("/")

    session["usuario_id"] = usuario.id
    session["nombre"] = usuario.nombre
    return redirect("/tareas")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")