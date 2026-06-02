from datetime import datetime, date
from typing import Optional


class TipoRaza:
    def __init__(
        self,
        nombre_raza: str,
        descripcion_raza: str,
        id_tipo_raza: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_tipo_raza = id_tipo_raza
        self.nombre_raza = nombre_raza
        self.descripcion_raza = descripcion_raza
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"TipoRaza(id={self.id_tipo_raza}, nombre='{self.nombre_raza}')"


class Raza:
    def __init__(
        self,
        id_tipo_raza: int,
        id_raza: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_raza = id_raza
        self.id_tipo_raza = id_tipo_raza
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Raza(id={self.id_raza}, id_tipo_raza={self.id_tipo_raza})"


class SexoMascota:
    def __init__(
        self,
        tipo_sexo_mascota: str,
        id_sexo_mascota: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_sexo_mascota = id_sexo_mascota
        self.tipo_sexo_mascota = tipo_sexo_mascota
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"SexoMascota(id={self.id_sexo_mascota}, tipo='{self.tipo_sexo_mascota}')"


class Mascota:
    def __init__(
        self,
        nombre_mascota: Optional[str] = None,
        id_raza: Optional[int] = None,
        id_sexo_mascota: Optional[int] = None,
        id_mascota: Optional[int] = None,
    ):
        self.id_mascota = id_mascota
        self.nombre_mascota = nombre_mascota
        self.id_raza = id_raza
        self.id_sexo_mascota = id_sexo_mascota

    def __repr__(self):
        return f"Mascota(id={self.id_mascota}, nombre='{self.nombre_mascota}')"


class Region:
    def __init__(
        self,
        nombre_region: str,
        id_region: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_region = id_region
        self.nombre_region = nombre_region
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Region(id={self.id_region}, nombre='{self.nombre_region}')"


class Comuna:
    def __init__(
        self,
        nombre_comuna: str,
        id_region: int,
        id_comuna: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_comuna = id_comuna
        self.nombre_comuna = nombre_comuna
        self.id_region = id_region
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Comuna(id={self.id_comuna}, nombre='{self.nombre_comuna}')"


class Direccion:
    def __init__(
        self,
        id_comuna: int,
        id_direccion: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_direccion = id_direccion
        self.id_comuna = id_comuna
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Direccion(id={self.id_direccion}, id_comuna={self.id_comuna})"


class Persona:
    def __init__(
        self,
        nombre: str,
        apellido: str,
        rut: Optional[str] = None,
        telefono: Optional[str] = None,
        fecha_nacimiento: Optional[date] = None,
        id_persona: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_persona = id_persona
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Persona(id={self.id_persona}, nombre='{self.nombre} {self.apellido}')"


class Empleado:
    def __init__(
        self,
        id_persona: int,
        id_direccion: int,
        id_empleado: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_empleado = id_empleado
        self.id_persona = id_persona
        self.id_direccion = id_direccion
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Empleado(id={self.id_empleado}, id_persona={self.id_persona})"


class Adoptante:
    def __init__(
        self,
        id_persona: int,
        id_direccion: int,
        id_adoptante: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_adoptante = id_adoptante
        self.id_persona = id_persona
        self.id_direccion = id_direccion
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Adoptante(id={self.id_adoptante}, id_persona={self.id_persona})"


class TipoUsuario:
    def __init__(
        self,
        nombre_tipo: str,
        id_tipo_usuario: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_tipo_usuario = id_tipo_usuario
        self.nombre_tipo = nombre_tipo
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"TipoUsuario(id={self.id_tipo_usuario}, nombre='{self.nombre_tipo}')"


class Usuario:
    def __init__(
        self,
        id_tipo_usuario: int,
        username: Optional[str] = None,
        fecha_registro: Optional[date] = None,
        ciudad: Optional[str] = None,
        edad: Optional[int] = None,
        id_usuario: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_usuario = id_usuario
        self.username = username
        self.fecha_registro = fecha_registro
        self.ciudad = ciudad
        self.edad = edad
        self.id_tipo_usuario = id_tipo_usuario
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Usuario(id={self.id_usuario}, username='{self.username}')"


class TipoEstado:
    def __init__(
        self,
        nombre_tipo: str,
        descripcion_tipo: str,
        id_tipo_estado: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_tipo_estado = id_tipo_estado
        self.nombre_tipo = nombre_tipo
        self.descripcion_tipo = descripcion_tipo
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"TipoEstado(id={self.id_tipo_estado}, nombre='{self.nombre_tipo}')"


class Estado:
    def __init__(
        self,
        id_tipo_estado: int,
        id_estado: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_estado = id_estado
        self.id_tipo_estado = id_tipo_estado
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return f"Estado(id={self.id_estado}, id_tipo_estado={self.id_tipo_estado})"


class SolicitudAdopcion:
    def __init__(
        self,
        id_mascota: int,
        id_adoptante: int,
        id_empleado: int,
        id_tipo_estado: int,
        fecha_solicitud: Optional[date] = None,
        id_solicitud_adopcion: Optional[int] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        deleted: bool = False,
    ):
        self.id_solicitud_adopcion = id_solicitud_adopcion
        self.id_mascota = id_mascota
        self.id_adoptante = id_adoptante
        self.id_empleado = id_empleado
        self.fecha_solicitud = fecha_solicitud or date.today()
        self.id_tipo_estado = id_tipo_estado
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.created_by = created_by
        self.updated_by = updated_by
        self.deleted = deleted

    def __repr__(self):
        return (
            f"SolicitudAdopcion(id={self.id_solicitud_adopcion}, "
            f"mascota={self.id_mascota}, adoptante={self.id_adoptante})"
        )