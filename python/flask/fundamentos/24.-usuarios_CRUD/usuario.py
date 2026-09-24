from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # 1. READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios ORDER BY id;"
        resultados = connectToMySQL("esquema_usuarios").query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios

    # 2. READ ONE BY ID
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {"id": id}
        resultados = connectToMySQL("esquema_usuarios").query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    # 3. CREATE
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL("esquema_usuarios").query_db(query, data)

    # 4. UPDATE
    @classmethod
    def update(cls, data):
        query = """
            UPDATE usuarios
            SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL("esquema_usuarios").query_db(query, data)

    # 5. DELETE
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL("esquema_usuarios").query_db(query, data)