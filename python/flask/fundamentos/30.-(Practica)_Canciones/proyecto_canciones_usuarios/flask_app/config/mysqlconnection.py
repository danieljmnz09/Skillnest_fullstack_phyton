import os
import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        # Conexión a la base de datos usando las credenciales del .env
        connection = pymysql.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "1234"),
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    # Método para ejecutar consultas SQL
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                cursor.execute(query, data)
                
                # Para registros creados retorna el nuevo ID
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                # Para consultas SELECT retorna la lista de resultados
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Error en la base de datos:", e)
                return False
            finally:
                self.connection.close()

# Función conectora por defecto
def connectToMySQL(db=None):
    if db is None:
        db = os.environ.get("DB_NAME")
    return MySQLConnection(db)