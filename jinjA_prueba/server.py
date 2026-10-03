from flask import Flask, render_template

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal ("/")
@app.route("/")
def inicio():
    # render_template busca el archivo dentro de la carpeta "templates"
    # y pasa la variable "usuario" hacia la plantilla de Jinja2
    return render_template("index.html", usuario="Floor")

if __name__ == "__main__":
    # Ejecutamos el servidor en modo desarrollo
    app.run(debug=True)