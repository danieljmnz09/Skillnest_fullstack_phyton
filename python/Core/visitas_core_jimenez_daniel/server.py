from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# Clave secreta obligatoria para poder manipular 'session'
app.secret_key = 'clave_secreta_contador_visitas'


# --- RUTA PRINCIPAL (Nivel 1, 2 y 3) ---
@app.route('/')
def index():
    # Comprobar si las propiedades existen en sesión; si no, inicializarlas
    if 'visitas' not in session:
        session['visitas'] = 0

    if 'reinicios' not in session:
        session['reinicios'] = 0

    # Incrementa +1 en cada visita a la ruta raíz
    session['visitas'] += 1

    return render_template('index.html')


# --- NIVEL 1: Destruir Sesión ---
@app.route('/destruir_sesion')
def destruir_sesion():
    # Elimina completamente todos los datos almacenados en sesión
    session.clear()
    return redirect('/')


# --- NIVEL 2 / BONUS DE PLATA: Sumar +2 Visitas ---
@app.route('/sumar_dos', methods=['POST'])
def sumar_dos():
    # Sumamos +1 aquí porque al redirigir a '/' se sumará +1 automáticamente (1 + 1 = 2)
    session['visitas'] = session.get('visitas', 0) + 1
    return redirect('/')


# --- NIVEL 2 Y 3 / BONUS DE PLATA Y ORO: Reiniciar a 0 y contar reinicios ---
@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    # Incrementar el contador de veces que se ha reiniciado
    session['reinicios'] = session.get('reinicios', 0) + 1
    # Fijamos en -1 para que, al redirigir a '/' y sumar 1, el valor quede exactamente en 0
    session['visitas'] = -1
    return redirect('/')


# --- NIVEL 3 / BONUS DE ORO: Incrementar valor personalizado ---
@app.route('/incrementar_custom', methods=['POST'])
def incrementar_custom():
    try:
        cantidad = int(request.form.get('cantidad', 1))
        # Restamos 1 a la cantidad enviada ya que la ruta '/' sumará 1 al procesar la redirección
        session['visitas'] = session.get('visitas', 0) + (cantidad - 1)
    except ValueError:
        pass
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)