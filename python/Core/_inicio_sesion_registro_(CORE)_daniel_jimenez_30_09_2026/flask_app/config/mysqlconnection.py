import os
import pymysql.cursors

# Conexión a la base de datos usando las variables del .env
class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                # Si es búsqueda, devuelvo la lista de datos
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                # Si es un nuevo registro, devuelvo su ID
                elif query.strip().lower().startswith("insert"):
                    return cursor.lastrowid
                else:
                    return None
            except Exception as e:
                print("Error en la base de datos:", e)
                return False
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)