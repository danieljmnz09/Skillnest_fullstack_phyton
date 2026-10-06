from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Categoria:
    BASE_DATOS = 'esquema_tasktrack'

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.usuario_id = data['usuario_id']
        self.cantidad_tareas = data.get('cantidad_tareas', 0)

    @classmethod
    def get_all_by_user(cls, usuario_id):
        # Consulta para traer las categorías con el conteo de tareas asignadas
        query = """
            SELECT c.*, COUNT(t.id) AS cantidad_tareas
            FROM categorias c
            LEFT JOIN tareas t ON c.id = t.categoria_id
            WHERE c.usuario_id = %(usuario_id)s
            GROUP BY c.id
            ORDER BY c.nombre ASC;
        """
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, {'usuario_id': usuario_id})
        categorias = []
        if resultados:
            for fila in resultados:
                categorias.append(cls(fila))
        return categorias

    @classmethod
    def save(cls, data):
        # Inserción en la base de datos asociando al usuario en sesión
        query = "INSERT INTO categorias (nombre, usuario_id) VALUES (%(nombre)s, %(usuario_id)s);"
        return connectToMySQL(cls.BASE_DATOS).query_db(query, data)

    @classmethod
    def get_by_name_and_user(cls, nombre, usuario_id):
        query = "SELECT * FROM categorias WHERE LOWER(nombre) = LOWER(%(nombre)s) AND usuario_id = %(usuario_id)s;"
        resultado = connectToMySQL(cls.BASE_DATOS).query_db(query, {'nombre': nombre, 'usuario_id': usuario_id})
        if resultado:
            return cls(resultado[0])
        return False

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM categorias WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL(cls.BASE_DATOS).query_db(query, data)

    @staticmethod
    def validar_categoria(datos, usuario_id):
        es_valido = True
        nombre = datos.get('nombre', '').strip()

        # Validación: Mínimo 3 caracteres según wireframe
        if len(nombre) < 3:
            flash("El nombre de la categoría debe tener al menos 3 caracteres.", "categoria")
            es_valido = False
        elif Categoria.get_by_name_and_user(nombre, usuario_id):
            flash("Ya tienes una categoría registrada con este nombre.", "categoria")
            es_valido = False

        return es_valido