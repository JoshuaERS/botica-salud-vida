from flask import Blueprint, render_template

bp = Blueprint("categorias", __name__, url_prefix="/categorias")


@bp.get("/")
def index():
    return render_template("modulo.html", titulo="Categorías")

