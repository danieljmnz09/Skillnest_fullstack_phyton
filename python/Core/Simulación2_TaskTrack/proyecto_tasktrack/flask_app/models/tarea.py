from datetime import datetime, date
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Tarea:
    db = "esquema_tasktrack"

    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']
        self.prioridad = data['prioridad']
        self.estado = data['estado']
        self.fecha_limite = data['fecha_limite']
        self.usuario_id = data['usuario_id']
        self.categoria_id = data['categoria_id']
        self.categoria_nombre = data.get('categoria_nombre', '')
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @property
    def dias_restantes(self):
        # Cálculo simple para mostrar los días faltantes en la tabla
        if self.fecha_limite:
            hoy = date.today()
            limite = self.fecha_limite if isinstance(self.fecha_limite, date) else datetime.strptime(str(self.fecha_limite), "%Y-%m-%d").date()
            dias = (limite - hoy).days
            return max(dias, 0)
        return 0

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO tareas (titulo, descripcion, prioridad, estado, fecha_limite, usuario_id, categoria_id)
        VALUES (%(titulo)s, %(descripcion)s, %(prioridad)s, 'Pendiente', %(fecha_limite)s, %(usuario_id)s, %(categoria_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_by_user(cls, usuario_id):
        query = """
        SELECT t.*, c.nombre AS categoria_nombre
        FROM tareas t
        INNER JOIN categorias c ON t.categoria_id = c.id
        WHERE t.usuario_id = %(usuario_id)s
        ORDER BY t.fecha_limite ASC;
        """
        results = connectToMySQL(cls.db).query_db(query, {'usuario_id': usuario_id})
        tareas = []
        if results:
            for row in results:
                tareas.append(cls(row))
        return tareas

    @classmethod
    def get_by_id(cls, id):
        query = """
        SELECT t.*, c.nombre AS categoria_nombre
        FROM tareas t
        INNER JOIN categorias c ON t.categoria_id = c.id
        WHERE t.id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, {'id': id})
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """
        UPDATE tareas 
        SET titulo = %(titulo)s, descripcion = %(descripcion)s, prioridad = %(prioridad)s,
            categoria_id = %(categoria_id)s, fecha_limite = %(fecha_limite)s
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update_estado(cls, data):
        query = "UPDATE tareas SET estado = %(estado)s WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM tareas WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validar_tarea(formulario):
        es_valido = True

        if len(formulario.get('titulo', '').strip()) < 3:
            flash("El título debe tener al menos 3 caracteres.", "tarea")
            es_valido = False

        if not formulario.get('categoria_id'):
            flash("Debes seleccionar una categoría.", "tarea")
            es_valido = False

        if not formulario.get('prioridad'):
            flash("Debes seleccionar una prioridad.", "tarea")
            es_valido = False

        if len(formulario.get('descripcion', '').strip()) < 10:
            flash("La descripción debe tener al menos 10 caracteres.", "tarea")
            es_valido = False

        if not formulario.get('fecha_limite'):
            flash("Debes seleccionar una fecha límite.", "tarea")
            es_valido = False
        else:
            # Validación de fecha no pasada
            fecha_ingresada = datetime.strptime(formulario['fecha_limite'], "%Y-%m-%d").date()
            if fecha_ingresada < date.today():
                flash("La fecha límite no puede ser en el pasado.", "tarea")
                es_valido = False

        return es_valido