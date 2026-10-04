from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.usuario import Usuario

# Redirigir la raíz a la página de usuarios
@app.route('/')
def index():
    return redirect(url_for('usuarios'))

# Muestra el formulario para nuevo usuario y el listado de usuarios
@app.route('/usuarios')
def usuarios():
    todos_usuarios = Usuario.get_all()
    return render_template('usuarios.html', usuarios=todos_usuarios)

# Procesar la creación de un nuevo usuario
@app.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    data = {
        'nombre': request.form['nombre'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    Usuario.save(data)
    return redirect(url_for('usuarios'))

# Mostrar detalle de usuario con sus canciones favoritas y el menú desplegable (BONUS)
@app.route('/usuarios/<int:id>')
def mostrar_usuario(id):
    data = {'id': id}
    usuario = Usuario.get_by_id_with_canciones(data)
    # BONUS: Trae solo las canciones que NO están en sus favoritos
    canciones_disponibles = Usuario.get_unfavorited_songs(data)
    return render_template('mostrar_usuario.html', usuario=usuario, canciones_disponibles=canciones_disponibles)

# Procesar la asignación de una canción favorita desde la página del usuario
@app.route('/usuarios/agregar_favorito', methods=['POST'])
def agregar_favorito_usuario():
    data = {
        'usuario_id': request.form['usuario_id'],
        'cancion_id': request.form['cancion_id']
    }
    Usuario.add_favorito(data)
    return redirect(url_for('mostrar_usuario', id=data['usuario_id']))