import re
from config.mysqlconnection import connectToMySQL
from flask import flash

# Expresión regular para validar el formato estándar de correo electrónico
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    BASE_DATOS = "esquema_usuarios"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def obtener_todos(cls):
        """Consulta todos los usuarios registrados en la base de datos."""
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query)
        usuarios = []
        if resultados:
            for fila in resultados:
                usuarios.append(cls(fila))
        return usuarios

    @classmethod
    def guardar(cls, data):
        """Inserta un nuevo registro de usuario en la tabla usuarios."""
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, data)

    @classmethod
    def obtener_por_email(cls, email):
        """Busca si el correo ya existe en la base de datos para garantizar que sea único."""
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': email}
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query, data)
        if len(resultados) < 1:
            return False
        return cls(resultados[0])

    @staticmethod
    def validar_usuario(formulario):
        """Valida los campos recibidos en el diccionario del formulario."""
        is_valid = True

        # 1. Validar que los campos no estén vacíos
        if len(formulario['nombre'].strip()) == 0:
            flash("El nombre es obligatorio.", "error")
            is_valid = False

        if len(formulario['apellido'].strip()) == 0:
            flash("El apellido es obligatorio.", "error")
            is_valid = False

        if len(formulario['email'].strip()) == 0:
            flash("El correo electrónico es obligatorio.", "error")
            is_valid = False
        # 2. Validar que el e-mail tenga el formato correcto con Regex
        elif not EMAIL_REGEX.match(formulario['email']):
            flash("E-mail inválido", "error")
            is_valid = False
        # 3. BONUS: Validar que el correo no esté registrado previamente
        elif Usuario.obtener_por_email(formulario['email']):
            flash("Este e-mail ya está registrado.", "error")
            is_valid = False

        return is_valid