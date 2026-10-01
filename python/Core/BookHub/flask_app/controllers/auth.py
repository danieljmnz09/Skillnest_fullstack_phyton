from functools import wraps
from flask import flash, redirect, render_template, request, session, url_for
from pymysql.err import IntegrityError
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario


def requiere_login(view):
    @wraps(view)
    def protegida(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Inicia sesión para continuar.", "warning")
            return redirect(url_for("inicio"))
        return view(*args, **kwargs)
    return protegida


@app.route("/")
def inicio():
    if "usuario_id" in session:
        return redirect(url_for("mis_libros"))
    return render_template("auth.html")


@app.post("/registro")
def registro():
    datos = request.form.to_dict()
    errores = Usuario.validar_registro(datos)
    if errores:
        for error in errores:
            flash(error, "danger")
        return redirect(url_for("inicio"))
    email = datos["email"].strip().lower()
    try:
        user_id = Usuario.crear({
            "name": datos["name"].strip(),
            "surname": datos["surname"].strip(),
            "email": email,
            "password_hash": bcrypt.generate_password_hash(datos["password"]).decode("utf-8"),
        })
    except IntegrityError:
        flash("Ese correo ya tiene una cuenta.", "danger")
        return redirect(url_for("inicio"))
    session.clear()
    session["usuario_id"] = user_id
    session["nombre_usuario"] = datos["name"].strip()
    flash("Tu cuenta está lista. Bienvenido a BookHub.", "success")
    return redirect(url_for("mis_libros"))


@app.post("/login")
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    usuario = Usuario.por_email(email) if email else None
    if not usuario or not bcrypt.check_password_hash(usuario["password_hash"], password):
        flash("Correo o contraseña incorrectos.", "danger")
        return redirect(url_for("inicio"))
    session.clear()
    session["usuario_id"] = usuario["id"]
    session["nombre_usuario"] = usuario["name"]
    return redirect(url_for("mis_libros"))


@app.post("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada.", "success")
    return redirect(url_for("inicio"))
