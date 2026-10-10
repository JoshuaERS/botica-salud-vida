from . import get_db


def listar_movimientos():
    return get_db().execute(
        "SELECT * FROM movimientos ORDER BY creado_en DESC"
    ).fetchall()

