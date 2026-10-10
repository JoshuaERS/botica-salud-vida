from flask import Blueprint, render_template

bp = Blueprint("productos", __name__, url_prefix="/productos")


@bp.get("/")
def index():
    return render_template("modulo.html", titulo="Productos")

