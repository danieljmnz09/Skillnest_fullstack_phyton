from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario

app = Flask(__name__)


# 1. Pagina principal: http://127.0.0.1:5000/usuarios
@app.route("/usuarios")
def usuarios():
    todos_los_usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=todos_los_usuarios)


# 2. Pagina formulario: http://127.0.0.1:5000/usuarios/nuevo
@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("usuario_nuevo.html")


# 3. Procesar formulario y redirigir
@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
    }
    Usuario.save(data)
    # Redirige exitosamente a la primera página /usuarios
    return redirect(url_for("usuarios"))


if __name__ == "__main__":
    app.run(debug=True)