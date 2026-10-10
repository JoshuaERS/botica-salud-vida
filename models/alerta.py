from datetime import date, timedelta

from . import get_db


def listar_stock_bajo():
    return get_db().execute(
        """
        SELECT p.id, p.nombre, p.stock_minimo,
               COALESCE(SUM(l.cantidad), 0) AS stock_actual
        FROM productos p
        LEFT JOIN lotes l ON l.producto_id = p.id
        GROUP BY p.id
        HAVING stock_actual <= p.stock_minimo
        ORDER BY stock_actual, p.nombre
        """
    ).fetchall()


def listar_proximos_a_vencer(dias=30):
    limite = (date.today() + timedelta(days=dias)).isoformat()
    return get_db().execute(
        """
        SELECT l.*, p.nombre AS producto
        FROM lotes l JOIN productos p ON p.id = l.producto_id
        WHERE l.cantidad > 0 AND l.fecha_vencimiento <= ?
        ORDER BY l.fecha_vencimiento, p.nombre
        """,
        (limite,),
    ).fetchall()

