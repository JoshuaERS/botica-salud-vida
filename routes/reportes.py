from flask import Blueprint, render_template

bp = Blueprint("reportes", __name__, url_prefix="/reportes")


@bp.get("/")
def index():
    return render_template("modulo.html", titulo="Reportes")

