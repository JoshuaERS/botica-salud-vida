from . import get_db


def listar_movimientos():
    return get_db().execute(
        """
        SELECT m.*, p.nombre AS producto, l.codigo AS lote
        FROM movimientos m
        JOIN productos p ON p.id = m.producto_id
        JOIN lotes l ON l.id = m.lote_id
        ORDER BY m.creado_en DESC, m.id DESC
        """
    ).fetchall()


def listar_lotes(producto_id=None):
    sql = """
        SELECT l.*, p.nombre AS producto
        FROM lotes l JOIN productos p ON p.id = l.producto_id
    """
    parametros = ()
    if producto_id:
        sql += " WHERE l.producto_id = ?"
        parametros = (producto_id,)
    return get_db().execute(sql + " ORDER BY l.fecha_vencimiento", parametros).fetchall()


def registrar_entrada(producto_id, codigo_lote, fecha_vencimiento, cantidad, observacion=""):
    database = get_db()
    with database:
        lote = database.execute(
            "SELECT id FROM lotes WHERE producto_id = ? AND codigo = ?",
            (producto_id, codigo_lote),
        ).fetchone()
        if lote:
            lote_id = lote["id"]
            database.execute(
                "UPDATE lotes SET cantidad = cantidad + ?, fecha_vencimiento = ? WHERE id = ?",
                (cantidad, fecha_vencimiento, lote_id),
            )
        else:
            cursor = database.execute(
                """
                INSERT INTO lotes (producto_id, codigo, fecha_vencimiento, cantidad)
                VALUES (?, ?, ?, ?)
                """,
                (producto_id, codigo_lote, fecha_vencimiento, cantidad),
            )
            lote_id = cursor.lastrowid
        database.execute(
            """
            INSERT INTO movimientos (producto_id, lote_id, tipo, cantidad, observacion)
            VALUES (?, ?, 'entrada', ?, ?)
            """,
            (producto_id, lote_id, cantidad, observacion),
        )


def registrar_salida(lote_id, cantidad, observacion=""):
    database = get_db()
    with database:
        lote = database.execute(
            "SELECT producto_id, cantidad FROM lotes WHERE id = ?", (lote_id,)
        ).fetchone()
        if lote is None:
            raise ValueError("El lote seleccionado no existe.")
        if lote["cantidad"] < cantidad:
            raise ValueError("La salida supera las unidades disponibles en el lote.")
        database.execute(
            "UPDATE lotes SET cantidad = cantidad - ? WHERE id = ?",
            (cantidad, lote_id),
        )
        database.execute(
            """
            INSERT INTO movimientos (producto_id, lote_id, tipo, cantidad, observacion)
            VALUES (?, ?, 'salida', ?, ?)
            """,
            (lote["producto_id"], lote_id, cantidad, observacion),
        )

