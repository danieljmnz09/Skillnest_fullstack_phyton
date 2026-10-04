import os
from flask_app.config.mysqlconnection import connectToMySQL

class Cancion:
    DB = os.environ.get("DB_NAME")

    # Constructor de la Canción
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuarios_favoritos = []

    # Guardar una nueva canción
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO canciones (titulo, artista)
            VALUES (%(titulo)s, %(artista)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    # Obtener todas las canciones
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones;"
        results = connectToMySQL(cls.DB).query_db(query)
        canciones = []
        if results:
            for c in results:
                canciones.append(cls(c))
        return canciones

    # Obtener una canción por ID con los usuarios a quienes les gusta (JOIN)
    @classmethod
    def get_by_id_with_usuarios(cls, data):
        from flask_app.models.usuario import Usuario

        query = """
            SELECT * FROM canciones 
            LEFT JOIN favoritos ON canciones.id = favoritos.cancion_id 
            LEFT JOIN usuarios ON usuarios.id = favoritos.usuario_id 
            WHERE canciones.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None

        cancion = cls(results[0])

        for row in results:
            if row['usuarios.id'] is not None:
                usuario_data = {
                    "id": row['usuarios.id'],
                    "nombre": row['nombre'],
                    "email": row['email'],
                    "password": row['password'],
                    "created_at": row['usuarios.created_at'],
                    "updated_at": row['usuarios.updated_at']
                }
                cancion.usuarios_favoritos.append(Usuario(usuario_data))

        return cancion

    # BONUS: Obtener usuarios que AÚN NO han agregado esta canción a sus favoritos
    @classmethod
    def get_unfavorited_users(cls, data):
        from flask_app.models.usuario import Usuario

        query = """
            SELECT * FROM usuarios 
            WHERE id NOT IN (
                SELECT usuario_id FROM favoritos WHERE cancion_id = %(id)s
            );
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        usuarios = []
        if results:
            for row in results:
                usuarios.append(Usuario(row))
        return usuarios