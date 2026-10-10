from . import get_db


def listar_productos(busqueda=""):
    termino = f"%{busqueda.strip()}%"
    return get_db().execute(
        """
        SELECT p.*, c.nombre AS categoria,
               COALESCE(SUM(l.cantidad), 0) AS stock_actual
        FROM productos p
        LEFT JOIN categorias c ON c.id = p.categoria_id
        LEFT JOIN lotes l ON l.producto_id = p.id
        WHERE p.nombre LIKE ?
        GROUP BY p.id
        ORDER BY p.nombre
        """,
        (termino,),
    ).fetchall()


def obtener_producto(producto_id):
    return get_db().execute(
        """
        SELECT p.*, c.nombre AS categoria,
               COALESCE(SUM(l.cantidad), 0) AS stock_actual
        FROM productos p
        LEFT JOIN categorias c ON c.id = p.categoria_id
        LEFT JOIN lotes l ON l.producto_id = p.id
        WHERE p.id = ?
        GROUP BY p.id
        """,
        (producto_id,),
    ).fetchone()


def crear_producto(nombre, descripcion, precio, stock_minimo, categoria_id):
    database = get_db()
    cursor = database.execute(
        """
        INSERT INTO productos (nombre, descripcion, precio, stock_minimo, categoria_id)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nombre, descripcion, precio, stock_minimo, categoria_id),
    )
    database.commit()
    return cursor.lastrowid

