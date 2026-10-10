import tempfile
import unittest
from pathlib import Path

from app import create_app
from config import Config
from models import get_db


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = "test"
    DATABASE = Path(tempfile.gettempdir()) / "botica_salud_vida_test.db"


class BoticaTestCase(unittest.TestCase):
    def setUp(self):
        TestConfig.DATABASE.unlink(missing_ok=True)
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

    def tearDown(self):
        TestConfig.DATABASE.unlink(missing_ok=True)

    def test_paginas_principales_responden(self):
        for ruta in ("/", "/productos/", "/inventario/", "/alertas/"):
            self.assertEqual(self.client.get(ruta).status_code, 200)

    def test_flujo_producto_entrada_y_salida(self):
        respuesta = self.client.post(
            "/productos/nuevo",
            data={
                "nombre": "Paracetamol 500 mg",
                "descripcion": "Caja",
                "categoria_id": "1",
                "precio": "5.50",
                "stock_minimo": "5",
            },
        )
        self.assertEqual(respuesta.status_code, 302)

        respuesta = self.client.post(
            "/inventario/entrada",
            data={
                "producto_id": "1",
                "codigo_lote": "L-001",
                "fecha_vencimiento": "2030-12-31",
                "cantidad": "10",
                "observacion": "Ingreso inicial",
            },
        )
        self.assertEqual(respuesta.status_code, 302)

        respuesta = self.client.post(
            "/inventario/salida",
            data={"lote_id": "1", "cantidad": "4", "observacion": "Venta"},
        )
        self.assertEqual(respuesta.status_code, 302)
        with self.app.app_context():
            lote = get_db().execute("SELECT cantidad FROM lotes WHERE id = 1").fetchone()
            self.assertEqual(lote["cantidad"], 6)

    def test_rechaza_salida_superior_al_stock(self):
        with self.app.app_context():
            database = get_db()
            database.execute(
                "INSERT INTO productos (nombre, precio, stock_minimo) VALUES ('Prueba', 1, 0)"
            )
            database.execute(
                "INSERT INTO lotes (producto_id, codigo, fecha_vencimiento, cantidad) VALUES (1, 'A', '2030-01-01', 2)"
            )
            database.commit()
        respuesta = self.client.post(
            "/inventario/salida",
            data={"lote_id": "1", "cantidad": "3"},
            follow_redirects=True,
        )
        self.assertIn("supera las unidades disponibles".encode(), respuesta.data)
        with self.app.app_context():
            cantidad = get_db().execute("SELECT cantidad FROM lotes WHERE id = 1").fetchone()[0]
            self.assertEqual(cantidad, 2)


if __name__ == "__main__":
    unittest.main()
