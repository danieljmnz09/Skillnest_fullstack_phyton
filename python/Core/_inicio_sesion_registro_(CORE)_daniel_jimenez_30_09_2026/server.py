# Arrancamos la app y cargamos las rutas
from flask_app import app
from flask_app.controllers import usuarios

if __name__ == "__main__":
    # Reinicia automáticamente la app si hacemos cambios
    app.run(debug=True)