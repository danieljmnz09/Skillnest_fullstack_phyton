from flask_app.config.mysqlconnection import connectToMySQL

class Inscripcion:
    @classmethod
    def inscribir_estudiante_en_curso(cls, datos):
        query = """
            INSERT INTO inscripciones (estudiante_id, curso_id)
            VALUES (%(estudiante_id)s, %(curso_id)s);
        """
        return connectToMySQL('esquema_educacion').query_db(query, datos)