import unittest
from datetime import date
from unittest.mock import patch

from flask_app import app
from flask_app.models.libro import Libro
from flask_app.models.usuario import Usuario

USUARIO = {"id": 7, "name": "Ana", "surname": "Luz", "email": "ana@example.com"}
LIBRO = {
    "id": 12,
    "title": "Cien años de soledad",
    "author": "Gabriel García Márquez",
    "genre": "Ficción",
    "published_on": date(1967, 5, 30),
    "description": "Una historia familiar.",
    "user_id": 7,
    "owner_name": "Ana",
    "owner_surname": "Luz",
    "favorite_count": 0,
    "is_favorite": 0,
}


class ValidacionesTest(unittest.TestCase):
    def test_registro_acepta_datos_validos(self):
        errores = Usuario.validar_registro({
            "name": "Ana",
            "surname": "Luz",
            "email": "ana@example.com",
            "password": "clave-segura",
            "confirm_password": "clave-segura",
        })
        self.assertEqual(errores, [])

    def test_libro_rechaza_campos_vacios_y_fecha_futura(self):
        errores = Libro.validar({
            "title": "", "author": "", "genre": "",
            "published_on": "2999-01-01", "description": "",
        })
        self.assertGreaterEqual(len(errores), 4)
        self.assertTrue(any("futura" in error for error in errores))


class RutasTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def iniciar_sesion_prueba(self):
        with self.client.session_transaction() as sesion:
            sesion["usuario_id"] = USUARIO["id"]
            sesion["nombre_usuario"] = USUARIO["name"]

    def test_vistas_privadas_redirigen_sin_sesion(self):
        for path in ("/libros", "/explorar", "/favoritos", "/libros/nuevo"):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 302)
                self.assertEqual(response.location, "/")

    def test_vistas_principales_renderizan_con_sesion(self):
        self.iniciar_sesion_prueba()
        with patch.object(Usuario, "por_id", return_value=USUARIO), patch.object(Libro, "listar", return_value=[]):
            for path in ("/libros", "/explorar", "/favoritos", "/libros/nuevo"):
                with self.subTest(path=path):
                    self.assertEqual(self.client.get(path).status_code, 200)

    def test_mis_libros_renderiza_tabla_comunitaria(self):
        self.iniciar_sesion_prueba()
        libro_comunidad = {**LIBRO, "id": 13, "user_id": 99, "owner_name": "Leo"}
        with patch.object(Usuario, "por_id", return_value=USUARIO), patch.object(
            Libro, "listar", side_effect=[[], [libro_comunidad]]
        ):
            response = self.client.get("/libros")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Libros de la comunidad", response.data)
        self.assertIn(b"Cien a\xc3\xb1os de soledad", response.data)

    def test_edicion_rechaza_libro_de_otro_usuario(self):
        self.iniciar_sesion_prueba()
        libro_ajeno = {**LIBRO, "user_id": 99}
        with patch.object(Usuario, "por_id", return_value=USUARIO), patch.object(Libro, "por_id", return_value=libro_ajeno):
            self.assertEqual(self.client.get("/libros/12/editar").status_code, 403)

    def test_borrado_solo_intenta_eliminar_con_id_del_usuario_actual(self):
        self.iniciar_sesion_prueba()
        with patch.object(Usuario, "por_id", return_value=USUARIO), patch.object(Libro, "eliminar", return_value=0) as eliminar:
            self.assertEqual(self.client.post("/libros/12/eliminar").status_code, 404)
            eliminar.assert_called_once_with(12, USUARIO["id"])


if __name__ == "__main__":
    unittest.main()
