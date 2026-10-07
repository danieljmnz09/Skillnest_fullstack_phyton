import re
from flask import flash
from flask_app import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL

# Expresión regular para validar el formato de correo
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    db = "esquema_tasktrack"

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        # Encriptamos la contraseña antes de guardar en la BD
        password_hash = bcrypt.generate_password_hash(data['password'])
        data_copia = dict(data)
        data_copia['password'] = password_hash
        
        query = """
        INSERT INTO usuarios (nombre, apellido, email, password)
        VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db).query_db(query, data_copia)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, {'email': email})
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, usuario_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, {'id': usuario_id})
        if not results:
            return False
        return cls(results[0])

    @staticmethod
    def validar_registro(formulario):
        es_valido = True

        # Validaciones de Registro según wireframe
        if len(formulario['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        if len(formulario['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        if not EMAIL_REGEX.match(formulario['email']):
            flash("Ingresa un correo electrónico con formato válido.", "registro")
            es_valido = False
        else:
            if Usuario.get_by_email(formulario['email']):
                flash("El correo electrónico ya está registrado.", "registro")
                es_valido = False

        if len(formulario['password']) < 6:
            flash("La contraseña debe tener al menos 6 caracteres.", "registro")
            es_valido = False

        if formulario['password'] != formulario['confirm_password']:
            flash("Las contraseñas no coinciden.", "registro")
            es_valido = False

        return es_valido

    @staticmethod
    def validar_login(formulario):
        usuario = Usuario.get_by_email(formulario['email'])
        if not usuario:
            flash("El email no está registrado.", "login")
            return False

        if not bcrypt.check_password_hash(usuario.password, formulario['password']):
            flash("La contraseña es incorrecta.", "login")
            return False

        return usuario