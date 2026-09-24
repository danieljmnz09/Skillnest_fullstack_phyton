from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)

# --- READ ALL ---
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)

# --- CREATE (FORM) ---
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")

# --- CREATE (POST) ---
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip()
    }
    Usuario.save(data)
    return redirect(url_for("usuarios"))

# --- READ ONE ---
@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)
    if usuario is None:
        return "Usuario no encontrado", 404
    return render_template("usuario.html", usuario=usuario)

# --- UPDATE (FORM) ---
@app.route("/usuarios/editar/<int:id>")
def editar_usuario(id):
    usuario = Usuario.get_by_id(id)
    if usuario is None:
        return "Usuario no encontrado", 404
    return render_template("usuario_editar.html", usuario=usuario)

# --- UPDATE (POST) ---
@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar_usuario(id):
    data = {
        "id": id,
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip()
    }
    Usuario.update(data)
    return redirect(url_for("usuarios"))

# --- DELETE ---
@app.route("/usuarios/borrar/<int:id>")
def borrar_usuario(id):
    Usuario.delete(id)
    return redirect(url_for("usuarios"))

if __name__ == "__main__":
    app.run(debug=True)