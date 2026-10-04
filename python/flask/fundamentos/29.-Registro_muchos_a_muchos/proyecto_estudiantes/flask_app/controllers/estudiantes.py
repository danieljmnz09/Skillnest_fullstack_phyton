from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.estudiante import Estudiante

@app.route("/estudiantes")
def listar_estudiantes():
    estudiantes = Estudiante.get_all()
    return render_template("estudiantes.html", estudiantes=estudiantes)

@app.route("/estudiantes/crear", methods=["POST"])
def crear_estudiante():
    datos = {
        "nombre": request.form["nombre"],
        "email": request.form["email"]
    }
    Estudiante.save(datos)
    return redirect("/estudiantes")

@app.route("/estudiantes/<int:id>")
def ver_estudiante(id):
    datos = {"id_estudiante": id}
    estudiante = Estudiante.get_estudiante_con_cursos(datos)
    return render_template("estudiante_detalle.html", estudiante=estudiante)