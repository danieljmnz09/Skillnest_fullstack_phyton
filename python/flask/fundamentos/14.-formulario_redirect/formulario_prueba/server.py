from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. Ruta Principal (Muestra el formulario)
@app.route("/")
def index():
    return render_template("index.html")

# 2. Ruta para procesar el formulario (Solo POST)
@app.route("/registrar", methods=["POST"])
def registrar():
    # Obtener datos mediante request.form
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")

    # Mostrar información en la terminal
    print("============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("============================")

    # Aplicar patrón PRG: Redireccionar vía GET a /mostrar
    return redirect(url_for("mostrar"))

# 3. Ruta de Confirmación (GET)
@app.route("/mostrar")
def mostrar():
    return render_template("mostrar.html")

# 4. Ruta de Ayuda (Desafío adicional)
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

if __name__ == "__main__":
    app.run(debug=True)