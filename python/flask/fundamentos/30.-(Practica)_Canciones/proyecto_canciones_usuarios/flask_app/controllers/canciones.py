from flask_app import app
from flask import render_template, redirect, request, url_for
from flask_app.models.cancion import Cancion
from flask_app.models.usuario import Usuario

# Muestra el formulario para nueva canción y el listado de canciones
@app.route('/canciones')
def canciones():
    todas_canciones = Cancion.get_all()
    return render_template('canciones.html', canciones=todas_canciones)

# Procesar la creación de una nueva canción
@app.route('/canciones/crear', methods=['POST'])
def crear_cancion():
    data = {
        'titulo': request.form['titulo'],
        'artista': request.form['artista']
    }
    Cancion.save(data)
    return redirect(url_for('canciones'))

# Mostrar detalle de canción con los usuarios que la agregaron y el menú desplegable (BONUS)
@app.route('/canciones/<int:id>')
def mostrar_cancion(id):
    data = {'id': id}
    cancion = Cancion.get_by_id_with_usuarios(data)
    # BONUS: Trae solo los usuarios que NO han agregado esta canción
    usuarios_disponibles = Cancion.get_unfavorited_users(data)
    return render_template('mostrar_cancion.html', cancion=cancion, usuarios_disponibles=usuarios_disponibles)

# Procesar la asignación de un usuario a una canción desde la página de la canción
@app.route('/canciones/agregar_favorito', methods=['POST'])
def agregar_favorito_cancion():
    data = {
        'usuario_id': request.form['usuario_id'],
        'cancion_id': request.form['cancion_id']
    }
    Usuario.add_favorito(data)
    return redirect(url_for('mostrar_cancion', id=data['cancion_id']))