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

from flask import Flask, render_template

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


# ==========================================
# Ejecutar aplicación
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)