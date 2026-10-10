from . import get_db


def listar_categorias():
    return get_db().execute("SELECT * FROM categorias ORDER BY nombre").fetchall()

