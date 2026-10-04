from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id_estudiante = data['id_estudiante']
        self.nombre = data['nombre']
        self.email = data['email']
        self.created_at = data['created_at']
        self.cursos = []

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO estudiantes (nombre, email) VALUES (%(nombre)s, %(email)s);"
        return connectToMySQL('esquema_educacion').query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM estudiantes;"
        resultados = connectToMySQL('esquema_educacion').query_db(query)
        estudiantes = []
        if resultados:
            for row in resultados:
                estudiantes.append(cls(row))
        return estudiantes

    @classmethod
    def get_estudiante_con_cursos(cls, datos):
        from flask_app.models.curso import Curso

        query = """
            SELECT 
                estudiantes.id_estudiante, estudiantes.nombre, estudiantes.email, estudiantes.created_at,
                cursos.id_curso, cursos.nombre_curso, cursos.descripcion, cursos.created_at AS curso_created_at
            FROM estudiantes
            LEFT JOIN inscripciones ON inscripciones.estudiante_id = estudiantes.id_estudiante
            LEFT JOIN cursos ON inscripciones.curso_id = cursos.id_curso
            WHERE estudiantes.id_estudiante = %(id_estudiante)s;
        """
        resultados = connectToMySQL('esquema_educacion').query_db(query, datos)
        if not resultados:
            return None

        estudiante = cls(resultados[0])
        for fila in resultados:
            if fila['id_curso'] is not None:
                datos_curso = {
                    "id_curso": fila['id_curso'],
                    "nombre_curso": fila['nombre_curso'],
                    "descripcion": fila['descripcion'],
                    "created_at": fila['curso_created_at']
                }
                estudiante.cursos.append(Curso(datos_curso))
        return estudiante