from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# Es obligatorio definir una clave secreta para poder usar la sesión (session)
app.secret_key = 'clave_secreta_super_segura'


# RUTA 1: Muestra el formulario inicial en http://localhost:5000/
@app.route('/')
def formulario():
    return render_template("index.html")


# RUTA 2: Recibe los datos vía POST, los guarda en la sesión y REDIRIGE
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    print("Recibiendo información del formulario:")
    print(request.form)

    # Guardamos la información dentro de 'session'
    session['nombre'] = request.form['nombre']
    session['email'] = request.form['email']

    # Redirigimos a la ruta GET
    return redirect('/mostrar_usuario')


# RUTA 3: Muestra la información leída desde la sesión
@app.route('/mostrar_usuario')
def mostrar_usuario():
    print("Usuario redirigido a /mostrar_usuario")
    return render_template("mostrar.html")


if __name__ == "__main__":
    app.run(debug=True)