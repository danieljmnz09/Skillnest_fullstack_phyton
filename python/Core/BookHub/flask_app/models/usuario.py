import re
from flask_app.config.mysqlconnection import query_db

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


class Usuario:
    @staticmethod
    def por_email(email):
        return query_db("SELECT * FROM users WHERE email = %(email)s", {"email": email}, fetchone=True)

    @staticmethod
    def por_id(user_id):
        return query_db(
            "SELECT id, name, surname, email FROM users WHERE id = %(id)s",
            {"id": user_id}, fetchone=True,
        )

    @staticmethod
    def crear(datos):
        return query_db(
            "INSERT INTO users (name, surname, email, password_hash) "
            "VALUES (%(name)s, %(surname)s, %(email)s, %(password_hash)s)",
            datos,
        )

    @staticmethod
    def validar_registro(datos):
        errores = []
        name = datos.get("name", "").strip()
        surname = datos.get("surname", "").strip()
        email = datos.get("email", "").strip().lower()
        password = datos.get("password", "")
        if len(name) < 2 or len(name) > 60:
            errores.append("El nombre debe tener entre 2 y 60 caracteres.")
        if len(surname) < 2 or len(surname) > 60:
            errores.append("El apellido debe tener entre 2 y 60 caracteres.")
        if len(email) > 150 or not EMAIL_RE.fullmatch(email):
            errores.append("Ingresa un correo electrónico válido.")
        if len(password) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")
        if password != datos.get("confirm_password", ""):
            errores.append("Las contraseñas no coinciden.")
        return errores
