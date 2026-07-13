from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return "🌎 ¡Bienvenido a nuestro servidor Flask!"

# Ruta genérica para explorar enrutamiento
@app.route("/explorar")
def exito():
    return "¿Que ruta estas buscando? ¡Prueba con diferentes direcciones!"

# Rutas dinámicas para personalización
@app.route("/perfil/<nombre>")
def perfil(nombre):
    return f"¡Hola {nombre} bienvenido a tu perfil personalizado en nuestra app."

# Ruta que repite un mensaje varias veces
@app.route("/repite/<int:veces>/<mensaje>")
def repite(mensaje, veces):
    return f"<h1>Repite despues de mi:<h1/> {mensaje}" * veces


# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente

# Ejecuta el servidor
if __name__ == "__main__":
   app.run(debug=True)