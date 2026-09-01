from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
# Clave necesaria para cifrar la cookie de sesión en el navegador
app.secret_key = "una-clave-secreta"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    # 1. Obtener datos de la petición POST
    nombre = request.form["nombre"]
    email = request.form["email"]
    ciudad = request.form["ciudad"]

    # 2. Guardar datos en session
    session["nombre_usuario"] = nombre
    session["email_usuario"] = email
    session["ciudad_usuario"] = ciudad

    # 3. Aplicar patrón PRG (Redirect vía GET)
    return redirect(url_for("mostrar_usuario"))

@app.route("/mostrar_usuario")
def mostrar_usuario():
    return render_template("mostrar.html")

@app.route("/perfil")
def perfil():
    # Desafío adicional: Vista de perfil que consume únicamente la sesión
    return render_template("perfil.html")

if __name__ == "__main__":
    app.run(debug=True)