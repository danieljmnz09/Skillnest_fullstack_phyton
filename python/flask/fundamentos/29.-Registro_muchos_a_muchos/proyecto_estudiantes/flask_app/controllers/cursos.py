from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.curso import Curso

@app.route("/cursos")
def listar_cursos():
    cursos = Curso.get_all()
    return render_template("cursos.html", cursos=cursos)

@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    datos = {
        "nombre_curso": request.form["nombre_curso"],
        "descripcion": request.form["descripcion"]
    }
    Curso.save(datos)
    return redirect("/cursos")

@app.route("/cursos/<int:id>")
def ver_curso(id):
    datos = {"id_curso": id}
    curso = Curso.get_curso_con_estudiantes(datos)
    return render_template("curso_detalle.html", curso=curso)