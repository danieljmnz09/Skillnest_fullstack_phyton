from flask import Flask, render_template, request, redirect, url_for
from mascota import Mascota
from mysqlconnection import connectToMySQL  # Importamos la conexión

app = Flask(__name__)


@app.route("/")
def index():
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)


@app.route("/crear_mascota", methods=["POST"])
def crear_mascota():
    datos = {
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "color": request.form["color"],
    }
    Mascota.save(datos)
    return redirect(url_for("index"))


# =========================================================
# RUTA TEMPORAL PARA VACIAR LA TABLA DESDE EL NAVEGADOR
# =========================================================
@app.route("/limpiar")
def limpiar():
    # Elimina todos los registros de la tabla mascotas
    connectToMySQL("primera_flask").query_db("TRUNCATE TABLE mascotas;")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)