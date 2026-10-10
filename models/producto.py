from . import get_db


def listar_productos():
    return get_db().execute("SELECT * FROM productos ORDER BY nombre").fetchall()

