"""
===========================================
Formulario de Prueba
===========================================

En esta aplicación aprenderemos cómo
recibir información enviada desde un
formulario HTML mediante el método POST.
"""

# ==========================================
# Importaciones
# ==========================================

# Flask:
# Framework principal.

# render_template:
# Permite mostrar plantillas HTML.

from flask import Flask, render_template, request, redirect

# ==========================================
# Crear aplicación Flask
# ==========================================

app = Flask(__name__)

# ==========================================
# Ruta principal
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario al usuario.

    En esta primera parte únicamente
    renderizaremos la página HTML.
    """

    return render_template("index.html")



@app.route("/crear_usuario", methods= "POST")
def crear_usuario():
    print("======== NUEVO USUARIO ========")
    print(request.form)
    print("---------------------------------")
    print("Nombre:", request.form[nombre])
    print("Correo:", request.form[email])
    print("Edad", request.form[Edad])
    print("Telefono", request.form[Telefono])
    print("---------------------------------")
   
    return render_template("index.html")

    #Nunca renderizamos una plantilla


# ==========================================
# Ejecutar aplicación
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)