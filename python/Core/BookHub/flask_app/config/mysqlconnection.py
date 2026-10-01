import os
import pymysql
import pymysql.cursors


def query_db(query, data=None, fetchone=False):
    connection = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "bookhub"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, data or {})
            if query.lstrip().lower().startswith("select"):
                return cursor.fetchone() if fetchone else cursor.fetchall()
            return cursor.lastrowid if query.lstrip().lower().startswith("insert") else cursor.rowcount
    finally:
        connection.close()
