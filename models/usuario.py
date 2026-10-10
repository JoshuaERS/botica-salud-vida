from . import get_db


def listar_usuarios():
    return get_db().execute("SELECT * FROM usuarios ORDER BY nombre").fetchall()

