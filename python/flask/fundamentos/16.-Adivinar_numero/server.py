from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "clave-secreta-adivina-numero"

MAX_INTENTOS = 5  # Constante para definir el límite

@app.route("/")
def index():
    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 10)
    if "intentos" not in session:
        session["intentos"] = 0
    if "mensaje" not in session:
        session["mensaje"] = f"Adivina un número entre 1 y 10. Tienes {MAX_INTENTOS} intentos."
    if "resultado" not in session:
        session["resultado"] = ""

    return render_template(
        "index.html",
        mensaje=session["mensaje"],
        resultado=session["resultado"],
        intentos=session["intentos"],
        max_intentos=MAX_INTENTOS
    )

@app.route("/adivinar", methods=["POST"])
def adivinar():
    # Si ya superó el límite, bloqueamos procesar más intentos
    if session.get("intentos", 0) >= MAX_INTENTOS or session.get("resultado") == "correcto":
        return redirect(url_for("index"))

    numero = int(request.form["numero"])
    numero_secreto = session["numero_secreto"]
    session["intentos"] += 1

    # Evaluar resultado
    if numero == numero_secreto:
        session["mensaje"] = f"¡Correcto! El número secreto era {numero_secreto}."
        session["resultado"] = "correcto"
    elif session["intentos"] >= MAX_INTENTOS:
        session["mensaje"] = f"💥 Game Over. Has agotado tus {MAX_INTENTOS} intentos. El número era {numero_secreto}."
        session["resultado"] = "perdió"
    elif numero < numero_secreto:
        session["mensaje"] = f"El número secreto es mayor que {numero}."
        session["resultado"] = "mayor"
    else:
        session["mensaje"] = f"El número secreto es menor que {numero}."
        session["resultado"] = "menor"

    return redirect(url_for("index"))

@app.route("/reiniciar")
def reiniciar():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)