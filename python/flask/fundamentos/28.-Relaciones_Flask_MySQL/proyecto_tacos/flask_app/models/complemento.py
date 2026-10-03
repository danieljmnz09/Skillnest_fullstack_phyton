from flask_app.config.mysqlconnection import connectToMySQL

class Complemento:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre_complemento = data["nombre_complemento"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.en_tacos = []

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO complementos (nombre_complemento) VALUES (%(nombre_complemento)s);"
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM complementos ORDER BY id;"
        resultados = connectToMySQL("esquema_tacos").query_db(query)
        complementos = []
        if resultados:
            for row in resultados:
                complementos.append(cls(row))
        return complementos

    @classmethod
    def asociar_taco(cls, datos):
        query = """
            INSERT INTO complementos_en_tacos (complemento_id, taco_id)
            VALUES (%(complemento_id)s, %(taco_id)s);
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    @classmethod
    def get_complementos_y_tacos(cls, datos):
        # Importación diferida dentro del método para evitar importación circular
        from flask_app.models.taco import Taco

        query = """
            SELECT 
                complementos.id AS id,
                complementos.nombre_complemento AS nombre_complemento,
                complementos.created_at AS created_at,
                complementos.updated_at AS updated_at,
                tacos.id AS taco_id,
                tacos.tortilla AS taco_tortilla,
                tacos.guiso AS taco_guiso,
                tacos.salsa AS taco_salsa,
                tacos.created_at AS taco_created_at,
                tacos.updated_at AS taco_updated_at
            FROM complementos
            LEFT JOIN complementos_en_tacos ON complementos_en_tacos.complemento_id = complementos.id
            LEFT JOIN tacos ON complementos_en_tacos.taco_id = tacos.id
            WHERE complementos.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query, datos)

        if not resultados:
            return None

        complemento = cls(resultados[0])

        for fila_en_db in resultados:
            if fila_en_db["taco_id"] is not None:
                datos_taco = {
                    "id": fila_en_db["taco_id"],
                    "tortilla": fila_en_db["taco_tortilla"],
                    "guiso": fila_en_db["taco_guiso"],
                    "salsa": fila_en_db["taco_salsa"],
                    "created_at": fila_en_db["taco_created_at"],
                    "updated_at": fila_en_db["taco_updated_at"]
                }
                complemento.en_tacos.append(Taco(datos_taco))

        return complemento