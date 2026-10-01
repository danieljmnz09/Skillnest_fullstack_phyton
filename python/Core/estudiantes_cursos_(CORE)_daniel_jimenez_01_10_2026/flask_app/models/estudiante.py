import os
from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    # Nombre de la BD obtenido del .env
    DB = os.environ.get("DB_NAME")

    # Constructor con los atributos del estudiante
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.curso_id = data['curso_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Método para guardar un nuevo estudiante en la BD
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
            VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)