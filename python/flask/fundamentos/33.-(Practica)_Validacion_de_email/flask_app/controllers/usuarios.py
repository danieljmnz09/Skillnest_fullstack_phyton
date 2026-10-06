from flask import render_template, request, redirect, session
from __init__ import app
from models.usuario import Usuario

@app.route('/')
def index():
    """Ruta principal: Muestra la lista de usuarios."""
    todos_los_usuarios = Usuario.obtener_todos()
    return render_template('index.html', usuarios=todos_los_usuarios)

@app.route('/usuarios/nuevo')
def nuevo_usuario():
    """Ruta GET: Muestra el formulario de creación."""
    return render_template('nuevo_usuario.html')

@app.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    """Ruta POST: Procesa la entrada del usuario."""
    # PISTA/BONUS: Guardamos en sesión los datos ingresados para no perderlos si ocurre un error
    session['datos_formulario'] = request.form

    # Si los datos ingresados no superan el validador, redirige de nuevo al formulario
    if not Usuario.validar_usuario(request.form):
        return redirect('/usuarios/nuevo')

    # Si la información es válida, se guarda el registro en la base de datos
    Usuario.guardar(request.form)

    # Limpiamos los datos guardados en sesión para reiniciar el formulario en el futuro
    session.pop('datos_formulario', None)

    # Redirige a la página principal
    return redirect('/')