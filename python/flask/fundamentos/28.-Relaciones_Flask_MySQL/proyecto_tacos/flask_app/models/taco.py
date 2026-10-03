from flask_app.config.mysqlconnection import connectToMySQL

class Taco:
    def __init__(self, data):
        self.id = data["id"]
        self.tortilla = data["tortilla"]
        self.guiso = data["guiso"]
        self.salsa = data["salsa"]
        self.restaurante_id = data.get("restaurante_id")
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.complementos = []

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO tacos (tortilla, guiso, salsa, restaurante_id)
            VALUES (%(tortilla)s, %(guiso)s, %(salsa)s, %(restaurante_id)s);
        """
        return connectToMySQL("esquema_tacos").query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tacos ORDER BY id;"
        resultados = connectToMySQL("esquema_tacos").query_db(query)
        tacos = []
        if resultados:
            for row in resultados:
                tacos.append(cls(row))
        return tacos

    @classmethod
    def get_taco_con_complementos(cls, datos):
        # Importación diferida
        from flask_app.models.complemento import Complemento

        query = """
            SELECT 
                tacos.id AS id,
                tacos.tortilla AS tortilla,
                tacos.guiso AS guiso,
                tacos.salsa AS salsa,
                tacos.created_at AS created_at,
                tacos.updated_at AS updated_at,
                complementos.id AS complemento_id,
                complementos.nombre_complemento AS complemento_nombre,
                complementos.created_at AS complemento_created_at,
                complementos.updated_at AS complemento_updated_at
            FROM tacos
            LEFT JOIN complementos_en_tacos ON complementos_en_tacos.taco_id = tacos.id
            LEFT JOIN complementos ON complementos_en_tacos.complemento_id = complementos.id
            WHERE tacos.id = %(id)s;
        """
        resultados = connectToMySQL("esquema_tacos").query_db(query, datos)

        if not resultados:
            return None

        taco_obj = cls(resultados[0])

        for fila in resultados:
            if fila["complemento_id"] is not None:
                datos_comp = {
                    "id": fila["complemento_id"],
                    "nombre_complemento": fila["complemento_nombre"],
                    "created_at": fila["complemento_created_at"],
                    "updated_at": fila["complemento_updated_at"]
                }
                taco_obj.complementos.append(Complemento(datos_comp))

        return taco_obj