from flask_app import app
# Importar los controladores para activar sus rutas
from flask_app.controllers import cursos, estudiantes

# Iniciar el servidor web en modo de depuración
if __name__ == "__main__":
    app.run(debug=True)