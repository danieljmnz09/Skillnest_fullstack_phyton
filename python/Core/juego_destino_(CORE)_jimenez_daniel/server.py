import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta_del_destino"

PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Grandes éxitos profesionales y financieros están por llegar a tu vida. Mantén la perseverancia.",
    "Un viaje inesperado cambiará tu perspectiva sobre el mundo y te abrirá nuevas puertas.",
    "Nuevas y valiosas amistades llegarán pronto para brindarte apoyo incondicional.",
    "Un proyecto personal al que le has dedicado tiempo finalmente dará frutos extraordinarios."
]

# Diccionario para traducir colores en español a valores válidos para CSS
COLORES_MAP = {
    "rojo": "red", "roja": "red",
    "verde": "green",
    "azul": "blue",
    "amarillo": "yellow", "amarilla": "yellow",
    "morado": "purple", "morada": "purple",
    "rosa": "pink", "rosado": "pink",
    "naranja": "orange",
    "negro": "black", "negra": "black",
    "blanco": "#ffffff", "blanca": "#ffffff",
    "gris": "gray",
    "violeta": "violet"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    color_ingresado = request.form.get("color", "verde").strip().lower()
    color_css = COLORES_MAP.get(color_ingresado, color_ingresado)

    # Guardar en sesión
    session["nombre"] = request.form.get("nombre", "Viajero")
    session["edad"] = request.form.get("edad", "18")
    session["color_texto"] = color_ingresado
    session["color_css"] = color_css
    session["animal"] = request.form.get("animal", "gato").lower()
    
    session["prediccion"] = random.choice(PREDICCIONES)
    session["numero_suerte"] = random.randint(1, 99)
    
    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    if "nombre" not in session:
        return redirect(url_for("index"))
    return render_template("futuro.html")

@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)