import os
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.estudiante import Estudiante

class Curso:
    # Nombre de la BD obtenido del .env
    DB = os.environ.get("DB_NAME")

    # Constructor del curso con una lista vacía para sus estudiantes
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.estudiantes = []

    # Obtener todos los cursos registrados
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL(cls.DB).query_db(query)
        cursos = []
        if results:
            for c in results:
                cursos.append(cls(c))
        return cursos

    # Guardar un nuevo curso
    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    # Obtener un curso específico junto a todos sus estudiantes (LEFT JOIN)
    @classmethod
    def get_by_id_with_estudiantes(cls, data):
        query = """
            SELECT * FROM cursos 
            LEFT JOIN estudiantes ON cursos.id = estudiantes.curso_id 
            WHERE cursos.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None
        
        # Se instancia el objeto Curso
        curso = cls(results[0])
        
        # Se vincula cada estudiante que pertenece a este curso
        for row in results:
            if row['estudiantes.id'] is not None:
                estudiante_data = {
                    "id": row['estudiantes.id'],
                    "nombre": row['estudiantes.nombre'],
                    "apellido": row['apellido'],
                    "edad": row['edad'],
                    "curso_id": row['curso_id'],
                    "created_at": row['estudiantes.created_at'],
                    "updated_at": row['estudiantes.updated_at']
                }
                curso.estudiantes.append(Estudiante(estudiante_data))
        return curso