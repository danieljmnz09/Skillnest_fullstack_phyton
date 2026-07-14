from flask import Flask, render_template
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return render_template("index.html",
     
     nombre = "Daniel",

     curso="Desarrollo Web con Flask",

     ciudad="Santiago",

     profesor=False,

    tecnologias=[ "Python", "Flask", "HTML", "CSS" ],

     anio=2026)

    
@app.route("/jugador")
def jugador():
    return render_template("jugador.html",
    jugador = "Daze",
    puntaje=100200,
    lider=True)

if __name__ == "__main__":
    app.run(debug=True)