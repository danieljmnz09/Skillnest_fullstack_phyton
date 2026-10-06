import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid
                return cursor.rowcount
            except Exception as e:
                print("Error en la base de datos:", e)
                return False
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)