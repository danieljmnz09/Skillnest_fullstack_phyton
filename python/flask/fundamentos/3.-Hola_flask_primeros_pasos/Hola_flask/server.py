from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Obrigado!"

@app.route("/nosotros")
def nosotros():
    return "¡Conocenos un poco más!"

@app.route("/sobremi")
def sobremi():
    return "¡Conoce un poco mas sobre mi!"

@app.route("/descripcion")
def descripcion():
    return "¡Descripciones!"

if __name__ == "__main__":
    app.run(debug=True)