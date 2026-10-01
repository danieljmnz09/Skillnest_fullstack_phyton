from datetime import date
from flask import abort, flash, redirect, render_template, request, session, url_for
from pymysql.err import MySQLError
from flask_app import app
from flask_app.controllers.auth import requiere_login
from flask_app.models.libro import Libro
from flask_app.models.usuario import Usuario


def _datos_formulario():
    return {
        "title": request.form.get("title", "").strip(),
        "author": request.form.get("author", "").strip(),
        "genre": request.form.get("genre", "").strip(),
        "published_on": request.form.get("published_on", "").strip(),
        "description": request.form.get("description", "").strip(),
    }


def _usuario_actual():
    usuario = Usuario.por_id(session["usuario_id"])
    if not usuario:
        session.clear()
        abort(401)
    return usuario


@app.get("/libros")
@requiere_login
def mis_libros():
    usuario = _usuario_actual()
    busqueda = request.args.get("q", "").strip()
    libros = Libro.listar(busqueda, usuario["id"], solo_usuario=True)
    comunidad = [libro for libro in Libro.listar(busqueda, usuario["id"])
                 if libro["user_id"] != usuario["id"]]
    return render_template("libros.html", libros=libros, comunidad=comunidad,
                           usuario=usuario, vista="mios", busqueda=busqueda)


@app.get("/explorar")
@requiere_login
def explorar():
    usuario = _usuario_actual()
    libros = [libro for libro in Libro.listar(request.args.get("q", "").strip(), usuario["id"])
              if libro["user_id"] != usuario["id"]]
    return render_template("libros.html", libros=libros, usuario=usuario, vista="comunidad", busqueda=request.args.get("q", ""))


@app.get("/favoritos")
@requiere_login
def favoritos():
    usuario = _usuario_actual()
    libros = Libro.listar(user_id=usuario["id"], solo_favoritos=True)
    return render_template("favoritos.html", libros=libros, usuario=usuario)


@app.route("/libros/nuevo", methods=["GET", "POST"])
@requiere_login
def nuevo_libro():
    usuario = _usuario_actual()
    if request.method == "GET":
        return render_template("form_libro.html", usuario=usuario, libro=None, hoy=date.today().isoformat())
    datos = _datos_formulario()
    errores = Libro.validar(datos)
    if errores:
        for error in errores:
            flash(error, "danger")
        return render_template("form_libro.html", usuario=usuario, libro=datos, hoy=date.today().isoformat()), 400
    datos["user_id"] = usuario["id"]
    try:
        book_id = Libro.crear(datos)
    except MySQLError:
        flash("No se pudo guardar el libro. Revisa la conexión con MySQL.", "danger")
        return render_template("form_libro.html", usuario=usuario, libro=datos, hoy=date.today().isoformat()), 503
    flash("Libro agregado a tu biblioteca.", "success")
    return redirect(url_for("detalle_libro", book_id=book_id))


@app.get("/libros/<int:book_id>")
@requiere_login
def detalle_libro(book_id):
    usuario = _usuario_actual()
    libro = Libro.por_id(book_id, usuario["id"])
    if not libro:
        abort(404)
    comunidad = Libro.usuarios_favoritos(book_id)
    return render_template("detalle.html", libro=libro, comunidad=comunidad, usuario=usuario)


@app.route("/libros/<int:book_id>/editar", methods=["GET", "POST"])
@requiere_login
def editar_libro(book_id):
    usuario = _usuario_actual()
    libro = Libro.por_id(book_id, usuario["id"])
    if not libro:
        abort(404)
    if libro["user_id"] != usuario["id"]:
        abort(403)
    if request.method == "GET":
        return render_template("form_libro.html", usuario=usuario, libro=libro, hoy=date.today().isoformat())
    datos = _datos_formulario()
    errores = Libro.validar(datos)
    if errores:
        for error in errores:
            flash(error, "danger")
        return render_template("form_libro.html", usuario=usuario, libro={**libro, **datos}, hoy=date.today().isoformat()), 400
    Libro.actualizar(book_id, usuario["id"], datos)
    flash("Cambios guardados.", "success")
    return redirect(url_for("detalle_libro", book_id=book_id))


@app.post("/libros/<int:book_id>/eliminar")
@requiere_login
def eliminar_libro(book_id):
    usuario = _usuario_actual()
    filas = Libro.eliminar(book_id, usuario["id"])
    if not filas:
        abort(404)
    flash("Libro eliminado de tu biblioteca.", "success")
    return redirect(url_for("mis_libros"))


@app.post("/libros/<int:book_id>/favorito")
@requiere_login
def alternar_favorito(book_id):
    usuario = _usuario_actual()
    if not Libro.alternar_favorito(book_id, usuario["id"]):
        abort(404)
    flash("Favorito actualizado.", "success")
    return redirect(request.referrer or url_for("explorar"))
