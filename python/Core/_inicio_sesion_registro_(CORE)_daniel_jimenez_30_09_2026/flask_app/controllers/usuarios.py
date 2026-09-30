from flask import render_template, request, redirect, session, flash, url_for
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

# Formulario principal
@app.route("/")
def index():
    # Si ya tiene sesión iniciada entra directo
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

# Procesar registro
@app.route("/registrar", methods=["POST"])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect(url_for("index"))

    # Encriptamos la contraseña antes de guardar en BD
    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    datos = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip().lower(),
        "password": pw_hash,
        "fecha_nacimiento": request.form["fecha_nacimiento"]
    }

    usuario_id = Usuario.save(datos)
    session["usuario_id"] = usuario_id
    flash("¡Te has registrado correctamente!", "exito")

    return redirect(url_for("dashboard"))

# Procesar login
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    usuario = Usuario.get_by_email(email)

    # Validar correo y contraseña encriptada
    if not usuario or not bcrypt.check_password_hash(usuario.password, password):
        flash("Correo o contraseña incorrectos.", "login_error")
        return redirect(url_for("index"))

    session["usuario_id"] = usuario.id
    return redirect(url_for("dashboard"))

# Vista protegida
@app.route("/dashboard")
def dashboard():
    # Bloquear acceso si no hay sesión
    if "usuario_id" not in session:
        flash("Debes iniciar sesión primero.", "login_error")
        return redirect(url_for("index"))

    usuario = Usuario.get_by_id(session["usuario_id"])
    if not usuario:
        session.clear()
        return redirect(url_for("index"))

    return render_template("dashboard.html", usuario=usuario)

# Salir y borrar sesión
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))