# Importamos la aplicación y los controladores para registrar las rutas
from flask_app import app
from flask_app.controllers import usuarios, tareas, categorias

# Ejecución del servidor local
if __name__ == "__main__":
    app.run(debug=True)