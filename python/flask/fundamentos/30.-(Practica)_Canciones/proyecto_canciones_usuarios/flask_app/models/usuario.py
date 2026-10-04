import os
from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    DB = os.environ.get("DB_NAME")

    # Constructor del Usuario
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.canciones_favoritas = []

    # Guardar un nuevo usuario
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, email, password)
            VALUES (%(nombre)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    # Obtener todos los usuarios
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.DB).query_db(query)
        usuarios = []
        if results:
            for u in results:
                usuarios.append(cls(u))
        return usuarios

    # Obtener un usuario por ID con sus canciones favoritas (JOIN)
    @classmethod
    def get_by_id_with_canciones(cls, data):
        # Importación local dentro del método para evitar importación circular
        from flask_app.models.cancion import Cancion

        query = """
            SELECT * FROM usuarios 
            LEFT JOIN favoritos ON usuarios.id = favoritos.usuario_id 
            LEFT JOIN canciones ON canciones.id = favoritos.cancion_id 
            WHERE usuarios.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return None

        usuario = cls(results[0])

        for row in results:
            if row['canciones.id'] is not None:
                cancion_data = {
                    "id": row['canciones.id'],
                    "titulo": row['titulo'],
                    "artista": row['artista'],
                    "created_at": row['canciones.created_at'],
                    "updated_at": row['canciones.updated_at']
                }
                usuario.canciones_favoritas.append(Cancion(cancion_data))

        return usuario

    # BONUS: Obtener solo las canciones que este usuario AÚN NO ha marcado como favoritas
    @classmethod
    def get_unfavorited_songs(cls, data):
        from flask_app.models.cancion import Cancion

        query = """
            SELECT * FROM canciones 
            WHERE id NOT IN (
                SELECT cancion_id FROM favoritos WHERE usuario_id = %(id)s
            );
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        canciones = []
        if results:
            for row in results:
                canciones.append(Cancion(row))
        return canciones

    # Agregar canción a los favoritos del usuario (Insertar en tabla intermedia)
    @classmethod
    def add_favorito(cls, data):
        query = """
            INSERT INTO favoritos (usuario_id, cancion_id)
            VALUES (%(usuario_id)s, %(cancion_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)