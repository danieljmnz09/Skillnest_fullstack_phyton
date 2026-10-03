from flask_app import app
from flask_app.controllers import tacos
from flask_app.controllers import complementos

if __name__ == "__main__":
    app.run(debug=True)