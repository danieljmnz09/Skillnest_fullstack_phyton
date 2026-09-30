import re
import os
from datetime import datetime, date
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# Reglas sencillas para revisar los campos
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBRE_REGEX = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')
# Mínimo 8 caracteres, 1 mayúscula y 1 número
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).{8,}$')

class Usuario:
    DB = os.getenv("DB_NAME", "esquema_login_registro")

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.fecha_nacimiento = data["fecha_nacimiento"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Insertar usuario en la base de datos
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password, fecha_nacimiento)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(fecha_nacimiento)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    # Buscar por email para verificar duplicados y para el login
    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {"email": email}
        resultado = connectToMySQL(cls.DB).query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return None

    # Buscar por ID para mostrar el perfil actual
    @classmethod
    def get_by_id(cls, usuario_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {"id": usuario_id}
        resultado = connectToMySQL(cls.DB).query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return None

    # Validaciones del registro
    @staticmethod
    def validar_registro(usuario):
        es_valido = True

        # Validar nombre y apellido
        if not usuario.get("nombre") or len(usuario["nombre"].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro_error")
            es_valido = False
        elif not NOMBRE_REGEX.match(usuario["nombre"].strip()):
            flash("El nombre solo puede contener letras.", "registro_error")
            es_valido = False

        if not usuario.get("apellido") or len(usuario["apellido"].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro_error")
            es_valido = False
        elif not NOMBRE_REGEX.match(usuario["apellido"].strip()):
            flash("El apellido solo puede contener letras.", "registro_error")
            es_valido = False

        # Validar email
        if not usuario.get("email") or not EMAIL_REGEX.match(usuario["email"].strip()):
            flash("Ingresa un correo válido.", "registro_error")
            es_valido = False
        elif Usuario.get_by_email(usuario["email"].strip().lower()):
            flash("Este correo ya está registrado.", "registro_error")
            es_valido = False

        # Validar si es mayor de edad (+18)
        if not usuario.get("fecha_nacimiento"):
            flash("Ingresa tu fecha de nacimiento.", "registro_error")
            es_valido = False
        else:
            try:
                fecha_nac = datetime.strptime(usuario["fecha_nacimiento"], "%Y-%m-%d").date()
                hoy = date.today()
                edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
                if edad < 18:
                    flash("Tienes que ser mayor de 18 años para registrarte.", "registro_error")
                    es_valido = False
            except ValueError:
                flash("Fecha no válida.", "registro_error")
                es_valido = False

        # Validar contraseña
        if not usuario.get("password") or not PASSWORD_REGEX.match(usuario["password"]):
            flash("La contraseña necesita mínimo 8 caracteres, una mayúscula y un número.", "registro_error")
            es_valido = False

        if usuario.get("password") != usuario.get("confirm_password"):
            flash("Las contraseñas no coinciden.", "registro_error")
            es_valido = False

        return es_valido