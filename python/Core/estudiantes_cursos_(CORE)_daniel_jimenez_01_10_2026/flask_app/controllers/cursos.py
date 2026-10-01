from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.curso import Curso

# Redirigir la ruta raíz a la vista de cursos
@app.route('/')
def index():
    return redirect(url_for('cursos'))

# Mostrar la página principal con el listado de cursos
@app.route('/cursos')
def cursos():
    todos_cursos = Curso.get_all()
    return render_template('cursos.html', cursos=todos_cursos)

# Procesar el formulario para crear un curso
@app.route('/cursos/crear', methods=['POST'])
def crear_curso():
    data = {'nombre': request.form['nombre']}
    Curso.save(data)
    return redirect(url_for('cursos'))

# Mostrar el detalle de un curso con sus estudiantes
@app.route('/cursos/<int:id>')
def mostrar_curso(id):
    data = {'id': id}
    curso_info = Curso.get_by_id_with_estudiantes(data)
    return render_template('mostrar_curso.html', curso=curso_info)