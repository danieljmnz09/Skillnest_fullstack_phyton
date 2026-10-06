from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    BASE_DATOS = 'esquema_seguidores'

    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email) 
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios ORDER BY nombre ASC;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query)
        usuarios = []
        if resultados:
            for row in resultados:
                usuarios.append(cls(row))
        return usuarios

    @classmethod
    def get_todas_relaciones_seguidores(cls):
        """
        Obtiene los pares (Usuario - Seguidor) para llenar la tabla superior.
        """
        query = """
            SELECT 
                CONCAT(u.nombre, ' ', u.apellido) AS usuario,
                CONCAT(s.nombre, ' ', s.apellido) AS seguidor
            FROM seguidores
            JOIN usuarios u ON seguidores.usuario_id = u.id
            JOIN usuarios s ON seguidores.seguidor_id = s.id
            ORDER BY u.nombre ASC;
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query)

    @classmethod
    def agregar_seguidor(cls, data):
        if data['usuario_id'] == data['seguidor_id']:
            return False  # Evita que un usuario se siga a sí mismo

        query = """
            INSERT IGNORE INTO seguidores (usuario_id, seguidor_id)
            VALUES (%(usuario_id)s, %(seguidor_id)s);
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, data)