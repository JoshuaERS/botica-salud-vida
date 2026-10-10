import tempfile
import unittest
from pathlib import Path

from app import create_app
from config import Config
from models import get_db


class CategoriaTestConfig(Config):
    TESTING = True
    SECRET_KEY = "test-categorias"
    DATABASE = Path(tempfile.gettempdir()) / "botica_categorias_test.db"


class CategoriasTestCase(unittest.TestCase):
    def setUp(self):
        CategoriaTestConfig.DATABASE.unlink(missing_ok=True)
        self.app = create_app(CategoriaTestConfig)
        self.client = self.app.test_client()

    def tearDown(self):
        CategoriaTestConfig.DATABASE.unlink(missing_ok=True)

    def test_pagina_responde(self):
        respuesta = self.client.get("/categorias/")
        self.assertEqual(respuesta.status_code, 200)

    def test_registra_categoria(self):
        respuesta = self.client.post(
            "/categorias/nueva",
            data={"nombre": "Vitaminas", "descripcion": "Suplementos"},
            follow_redirects=True,
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("Vitaminas".encode("utf-8"), respuesta.data)

    def test_rechaza_nombre_vacio(self):
        respuesta = self.client.post(
            "/categorias/nueva",
            data={"nombre": "   ", "descripcion": "Inválida"},
            follow_redirects=True,
        )
        self.assertIn("obligatorio".encode("utf-8"), respuesta.data)

    def test_rechaza_duplicada(self):
        datos = {"nombre": "Vitaminas", "descripcion": "Suplementos"}
        self.client.post("/categorias/nueva", data=datos)
        respuesta = self.client.post("/categorias/nueva", data=datos, follow_redirects=True)
        self.assertIn("Ya existe".encode("utf-8"), respuesta.data)
        with self.app.app_context():
            total = get_db().execute(
                "SELECT COUNT(*) FROM categorias WHERE nombre = ?", ("Vitaminas",)
            ).fetchone()[0]
            self.assertEqual(total, 1)


if __name__ == "__main__":
    unittest.main()