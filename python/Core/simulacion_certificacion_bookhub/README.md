# BookHub

Aplicación de biblioteca comunitaria con Flask, MySQL, PyMySQL, Jinja2, Bootstrap y arquitectura MVC modularizada.

## Requisitos

- Python 3.10 o posterior
- MySQL 8.0 o compatible

## Instalación

Desde esta carpeta del proyecto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edita `.env` con las credenciales de tu servidor MySQL y cambia `SECRET_KEY` por un valor aleatorio. Crea la base y las tablas ejecutando `schema.sql` en MySQL Workbench o con:

```powershell
Get-Content schema.sql | mysql -u root -p
```

Inicia la aplicación:

```powershell
python server.py
```

Abre `http://127.0.0.1:5000`. Crea una cuenta desde la pantalla inicial para comenzar a registrar libros.

## Funcionalidades

- Registro e inicio de sesión con contraseñas protegidas por Bcrypt y sesiones.
- CRUD de libros con validación de título, autor, género, fecha y descripción.
- Biblioteca personal y exploración comunitaria con búsqueda.
- Favoritos y visualización de los lectores que guardaron cada libro.
- Autorización por propietario en la edición y eliminación de libros.
- ERD en `flask_app/resources/ERD.md`.

## Estructura

- `flask_app/controllers/`: rutas y flujo MVC.
- `flask_app/models/`: consultas y validaciones de negocio.
- `flask_app/templates/`: vistas Jinja2.
- `flask_app/static/`: estilos.
- `schema.sql`: creación de la base de datos.
- `flask_app/resources/ERD.md`: diagrama entidad-relación Mermaid.

Para las capturas de entrega, inicia sesión con dos cuentas de prueba y captura la biblioteca, el formulario de alta, el detalle con lectores y la lista de favoritos.
