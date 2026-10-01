from flask_app.config.mysqlconnection import query_db


class Libro:
    @staticmethod
    def listar(query="", user_id=None, solo_usuario=False, solo_favoritos=False):
        filtros = []
        datos = {"user_id": user_id, "query": f"%{query}%"}
        if solo_usuario:
            filtros.append("b.user_id = %(user_id)s")
        if solo_favoritos:
            filtros.append("f.user_id = %(user_id)s")
        if query:
            filtros.append("(b.title LIKE %(query)s OR b.author LIKE %(query)s OR b.genre LIKE %(query)s)")
        where = f"WHERE {' AND '.join(filtros)}" if filtros else ""
        sql = f"""
            SELECT b.id, b.title, b.author, b.genre, b.published_on, b.description,
                   b.user_id, u.name AS owner_name, u.surname AS owner_surname,
                   COUNT(DISTINCT all_favorites.user_id) AS favorite_count,
                   MAX(CASE WHEN f.user_id = %(user_id)s THEN 1 ELSE 0 END) AS is_favorite
            FROM books b
            JOIN users u ON u.id = b.user_id
            LEFT JOIN favorites all_favorites ON all_favorites.book_id = b.id
            LEFT JOIN favorites f ON f.book_id = b.id AND f.user_id = %(user_id)s
            {where}
            GROUP BY b.id, u.id
            ORDER BY b.created_at DESC
        """
        return query_db(sql, datos)

    @staticmethod
    def por_id(book_id, user_id):
        return query_db("""
            SELECT b.id, b.title, b.author, b.genre, b.published_on, b.description,
                   b.user_id, u.name AS owner_name, u.surname AS owner_surname,
                   COUNT(DISTINCT all_favorites.user_id) AS favorite_count,
                   MAX(CASE WHEN mine.user_id = %(user_id)s THEN 1 ELSE 0 END) AS is_favorite
            FROM books b
            JOIN users u ON u.id = b.user_id
            LEFT JOIN favorites all_favorites ON all_favorites.book_id = b.id
            LEFT JOIN favorites mine ON mine.book_id = b.id AND mine.user_id = %(user_id)s
            WHERE b.id = %(book_id)s
            GROUP BY b.id, u.id
        """, {"book_id": book_id, "user_id": user_id}, fetchone=True)

    @staticmethod
    def usuarios_favoritos(book_id):
        return query_db("""
            SELECT u.id, u.name, u.surname
            FROM favorites f JOIN users u ON u.id = f.user_id
            WHERE f.book_id = %(book_id)s ORDER BY u.name, u.surname
        """, {"book_id": book_id})

    @staticmethod
    def crear(datos):
        return query_db("""
            INSERT INTO books (title, author, genre, published_on, description, user_id)
            VALUES (%(title)s, %(author)s, %(genre)s, %(published_on)s, %(description)s, %(user_id)s)
        """, datos)

    @staticmethod
    def actualizar(book_id, user_id, datos):
        return query_db("""
            UPDATE books SET title = %(title)s, author = %(author)s, genre = %(genre)s,
                published_on = %(published_on)s, description = %(description)s
            WHERE id = %(id)s AND user_id = %(user_id)s
        """, {**datos, "id": book_id, "user_id": user_id})

    @staticmethod
    def eliminar(book_id, user_id):
        return query_db("DELETE FROM books WHERE id = %(id)s AND user_id = %(user_id)s",
                        {"id": book_id, "user_id": user_id})

    @staticmethod
    def alternar_favorito(book_id, user_id):
        if not query_db("SELECT id FROM books WHERE id = %(id)s", {"id": book_id}, fetchone=True):
            return False
        favorito = query_db("SELECT book_id FROM favorites WHERE book_id = %(book_id)s AND user_id = %(user_id)s",
                            {"book_id": book_id, "user_id": user_id}, fetchone=True)
        if favorito:
            query_db("DELETE FROM favorites WHERE book_id = %(book_id)s AND user_id = %(user_id)s",
                     {"book_id": book_id, "user_id": user_id})
        else:
            query_db("INSERT INTO favorites (book_id, user_id) VALUES (%(book_id)s, %(user_id)s)",
                     {"book_id": book_id, "user_id": user_id})
        return True

    @staticmethod
    def validar(datos):
        errores = []
        for campo, etiqueta, limite in (("title", "El título", 160), ("author", "El autor", 120),
                                        ("genre", "El género", 60)):
            valor = datos.get(campo, "").strip()
            if not valor or len(valor) > limite:
                errores.append(f"{etiqueta} es obligatorio y no puede superar {limite} caracteres.")
        description = datos.get("description", "").strip()
        if not description or len(description) > 3000:
            errores.append("La descripción es obligatoria y debe tener máximo 3000 caracteres.")
        try:
            from datetime import date
            published = date.fromisoformat(datos.get("published_on", ""))
            if published > date.today():
                errores.append("La fecha de publicación no puede ser futura.")
        except ValueError:
            errores.append("Selecciona una fecha de publicación válida.")
        return errores
