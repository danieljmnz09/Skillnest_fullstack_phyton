import pymysql
from pymysql.cursors import DictCursor


class MySQLConnection:

    def __init__(self, db):
        self.db = db

    def connect(self):
        return pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database=self.db,
            charset="utf8mb4",
            cursorclass=DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):

        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute(query, data)

            if query.strip().lower().startswith("select"):
                result = cursor.fetchall()
                return result

            elif query.strip().lower().startswith("insert"):
                return cursor.lastrowid

            else:
                return None

        except Exception as e:
            print("Error en la consulta:", e)
            return False

        finally:
            cursor.close()
            connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)