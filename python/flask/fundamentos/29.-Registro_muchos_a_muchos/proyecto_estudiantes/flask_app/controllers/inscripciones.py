from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.inscripcion import Inscripcion
from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso

@app.route("/")
def index():
    estudiantes = Estudiante.get_all()
    cursos = Curso.get_all()
    return render_template("index.html", estudiantes=estudiantes, cursos=cursos)

@app.route("/inscribir", methods=["POST"])
def inscribir():
    datos = {
        "estudiante_id": request.form["estudiante_id"],
        "curso_id": request.form["curso_id"]
    }
    Inscripcion.inscribir_estudiante_en_curso(datos)
    return redirect("/")