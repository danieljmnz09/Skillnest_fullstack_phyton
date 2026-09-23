from mysqlconnection import connectToMySQL


class Mascota:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """Obtiene todas las mascotas de la base de datos."""
        query = """
            SELECT id, nombre, tipo, color, created_at, updated_at
            FROM mascotas
            ORDER BY id;
        """
        resultados = connectToMySQL("primera_flask").query_db(query)

        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas

    @classmethod
    def save(cls, datos):
        """Guarda una nueva mascota utilizando sentencia preparada."""
        query = """
            INSERT INTO mascotas (nombre, tipo, color, created_at, updated_at)
            VALUES (%(nombre)s, %(tipo)s, %(color)s, NOW(), NOW());
        """
        return connectToMySQL("primera_flask").query_db(query, datos)
        