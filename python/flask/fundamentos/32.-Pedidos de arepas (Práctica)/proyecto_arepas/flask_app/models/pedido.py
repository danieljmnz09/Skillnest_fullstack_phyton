from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Pedido:
    BASE_DATOS = 'esquema_arepas'

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.cantidad = data['cantidad']
        self.relleno = data['relleno']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pedidos ORDER BY created_at DESC;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query)
        pedidos = []
        if resultados:
            for fila in resultados:
                pedidos.append(cls(fila))
        return pedidos

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO pedidos (nombre, cantidad, relleno)
            VALUES (%(nombre)s, %(cantidad)s, %(relleno)s);
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, data)

    @staticmethod
    def validar_pedido(datos):
        es_valido = True

        nombre = datos.get('nombre', '').strip()
        cantidad_str = datos.get('cantidad', '').strip()
        relleno = datos.get('relleno', '').strip()

        # Validar campos vacíos
        if not nombre or not cantidad_str or not relleno:
            flash("Todos los campos son obligatorios", "pedido_error")
            return False

        # Validar longitud del nombre
        if len(nombre) < 2:
            flash("El nombre debe tener al menos 2 caracteres", "pedido_error")
            es_valido = False

        # Validar cantidad
        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                flash("Ingrese una cantidad válida", "pedido_error")
                es_valido = False
        except ValueError:
            flash("Ingrese una cantidad válida", "pedido_error")
            es_valido = False

        return es_valido