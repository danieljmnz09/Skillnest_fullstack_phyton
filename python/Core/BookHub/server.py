from flask_app import app
from flask_app.controllers import auth, libros


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
