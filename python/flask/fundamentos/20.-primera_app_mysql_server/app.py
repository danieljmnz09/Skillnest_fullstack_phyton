from flask import Flask, render_template
from mascota import Mascota

app = Flask(__name__)

@app.route("/")
def index():
    mascotas = Mascota.get_all()

    print(mascotas)

    return render_template("index.html", todas_mascotas=mascotas)


@app.route("/mascotas/perros")
def mostrar_perros():
    perros = Mascota.get_perros()

    return render_template("index.html", todas_mascotas=perros)


if __name__ == "__main__":
    app.run(debug=True)