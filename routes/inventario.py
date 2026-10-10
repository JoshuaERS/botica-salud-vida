from flask import Blueprint, render_template

bp = Blueprint("inventario", __name__, url_prefix="/inventario")


@bp.get("/")
def index():
    return render_template("modulo.html", titulo="Inventario")

