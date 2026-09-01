from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de Frutas Disponible (Imágenes actualizadas a .jpg)
FRUTAS = [
    {"id": 1, "nombre": "Manzana", "precio": 2.50, "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C.", "imagen": "manzana.jpg"},
    {"id": 2, "nombre": "Plátano", "precio": 1.80, "descripcion": "Fruta energética rica en potasio, perfecta para deportistas.", "imagen": "platano.jpg"},
    {"id": 3, "nombre": "Naranja", "precio": 3.00, "descripcion": "Cítrico jugoso con alto contenido de vitamina C y antioxidantes.", "imagen": "naranja.jpg"},
    {"id": 4, "nombre": "Fresa", "precio": 4.50, "descripcion": "Baya dulce y aromática, rica en antioxidantes y vitamina C.", "imagen": "fresa.jpg"},
    {"id": 5, "nombre": "Uva", "precio": 3.80, "descripcion": "Fruta pequeña y dulce, ideal para snacks y postres.", "imagen": "uva.jpg"},
    {"id": 6, "nombre": "Piña", "precio": 5.00, "descripcion": "Fruta tropical dulce y ácida, con propiedades antiinflamatorias.", "imagen": "piña.jpg"},
    {"id": 7, "nombre": "Sandía", "precio": 4.20, "descripcion": "Fruta refrescante, compuesta en un 90% de agua, ideal para el verano.", "imagen": "sandia.jpg"},
    {"id": 8, "nombre": "Mango", "precio": 3.50, "descripcion": "Fruta tropical dulce y aromática, rica en vitaminas A y C.", "imagen": "mango.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html', frutas=FRUTAS)

@app.route('/frutas')
@app.route('/fruta')
def frutas_catalogo():
    return render_template('frutas.html', frutas=FRUTAS)

# Procesa la orden enviada desde index.html
@app.route('/crear-orden', methods=['POST'])
def crear_orden():
    nombre = request.form.get('nombre', '')
    email = request.form.get('email', '')
    direccion = request.form.get('direccion', '')

    pedido_items = []
    total_frutas = 0
    total_pagar = 0.0

    # Iteramos para ver qué frutas compró el usuario
    for fruta in FRUTAS:
        cant_input = request.form.get(f'cantidad_{fruta["id"]}', '0')
        try:
            cantidad = int(cant_input)
        except ValueError:
            cantidad = 0

        if cantidad > 0:
            subtotal = fruta['precio'] * cantidad
            pedido_items.append({
                'nombre': fruta['nombre'],
                'precio': fruta['precio'],
                'cantidad': cantidad,
                'subtotal': subtotal,
                'imagen': fruta['imagen']
            })
            total_frutas += cantidad
            total_pagar += subtotal

    cliente = {
        'nombre': nombre,
        'email': email,
        'direccion': direccion
    }

    return render_template('checkout.html', cliente=cliente, pedido_items=pedido_items, total_frutas=total_frutas, total_pagar=total_pagar)

# Muestra el checkout de ejemplo con .jpg
@app.route('/checkout', methods=['GET'])
def checkout():
    cliente_demo = {
        'nombre': 'Joe',
        'email': 'joe@doe.com',
        'direccion': 'Alameda #1219'
    }
    
    items_demo = [
        {'nombre': 'Manzana', 'precio': 2.50, 'cantidad': 2, 'subtotal': 5.00, 'imagen': 'manzana.jpg'},
        {'nombre': 'Plátano', 'precio': 1.80, 'cantidad': 2, 'subtotal': 3.60, 'imagen': 'platano.jpg'},
        {'nombre': 'Naranja', 'precio': 3.00, 'cantidad': 1, 'subtotal': 3.00, 'imagen': 'naranja.jpg'},
    ]
    
    total_frutas = sum(item['cantidad'] for item in items_demo)
    total_pagar = sum(item['subtotal'] for item in items_demo)

    return render_template('checkout.html', cliente=cliente_demo, pedido_items=items_demo, total_frutas=total_frutas, total_pagar=total_pagar)

if __name__ == '__main__':
    app.run(debug=True)