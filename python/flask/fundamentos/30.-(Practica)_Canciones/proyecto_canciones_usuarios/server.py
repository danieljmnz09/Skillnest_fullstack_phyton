from flask_app import app
# Importar controladores para registrar sus rutas
from flask_app.controllers import usuarios, canciones

# Ejecutar la aplicación en modo desarrollo
if __name__ == "__main__":
    app.run(debug=True)