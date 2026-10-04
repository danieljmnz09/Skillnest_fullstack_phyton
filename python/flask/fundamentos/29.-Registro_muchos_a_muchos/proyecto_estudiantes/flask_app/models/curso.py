from flask_app.config.mysqlconnection import connectToMySQL

class Curso:
    def __init__(self, data):
        self.id_curso = data['id_curso']
        self.nombre_curso = data['nombre_curso']
        self.descripcion = data['descripcion']
        self.created_at = data['created_at']
        self.estudiantes = []

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO cursos (nombre_curso, descripcion) VALUES (%(nombre_curso)s, %(descripcion)s);"
        return connectToMySQL('esquema_educacion').query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        resultados = connectToMySQL('esquema_educacion').query_db(query)
        cursos = []
        if resultados:
            for row in resultados:
                cursos.append(cls(row))
        return cursos

    @classmethod
    def get_curso_con_estudiantes(cls, datos):
        from flask_app.models.estudiante import Estudiante

        query = """
            SELECT 
                cursos.id_curso, cursos.nombre_curso, cursos.descripcion, cursos.created_at,
                estudiantes.id_estudiante, estudiantes.nombre, estudiantes.email, estudiantes.created_at AS estudiante_created_at
            FROM cursos
            LEFT JOIN inscripciones ON inscripciones.curso_id = cursos.id_curso
            LEFT JOIN estudiantes ON inscripciones.estudiante_id = estudiantes.id_estudiante
            WHERE cursos.id_curso = %(id_curso)s;
        """
        resultados = connectToMySQL('esquema_educacion').query_db(query, datos)
        if not resultados:
            return None

        curso = cls(resultados[0])
        for fila in resultados:
            if fila['id_estudiante'] is not None:
                datos_estudiante = {
                    "id_estudiante": fila['id_estudiante'],
                    "nombre": fila['nombre'],
                    "email": fila['email'],
                    "created_at": fila['estudiante_created_at']
                }
                curso.estudiantes.append(Estudiante(datos_estudiante))
        return curso