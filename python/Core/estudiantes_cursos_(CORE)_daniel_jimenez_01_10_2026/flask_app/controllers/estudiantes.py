from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

# Mostrar formulario para crear estudiante (pasa los cursos para el <select>)
@app.route('/estudiantes/nuevo')
def nuevo_estudiante():
    todos_cursos = Curso.get_all()
    return render_template('nuevo_estudiante.html', cursos=todos_cursos)

# Procesar la creación de un estudiante
@app.route('/estudiantes/crear', methods=['POST'])
def crear_estudiante():
    data = {
        'curso_id': request.form['curso_id'],
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'edad': request.form['edad']
    }
    Estudiante.save(data)
    # Redirige a la vista del curso donde se agregó al estudiante
    return redirect(url_for('mostrar_curso', id=data['curso_id']))