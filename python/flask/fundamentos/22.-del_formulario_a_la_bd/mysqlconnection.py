import pymysql.cursors


class MySQLConnection:

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",  # Cambia por tu usuario de MySQL
            password="1234",  # Cambia por tu contraseña de MySQL
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)

                # Si es un SELECT, devuelve los registros
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                # Si es un INSERT, devuelve el ID generado
                elif query.strip().lower().startswith("insert"):
                    return cursor.lastrowid

                else:
                    return None

            except Exception as e:
                print("Error en la consulta SQL:", e)
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)