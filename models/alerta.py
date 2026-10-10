from . import get_db


def listar_alertas_pendientes():
    return get_db().execute(
        "SELECT * FROM alertas WHERE atendida = 0 ORDER BY creado_en DESC"
    ).fetchall()

