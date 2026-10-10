from flask import Blueprint, render_template

bp = Blueprint("alertas", __name__, url_prefix="/alertas")


@bp.get("/")
def index():
    return render_template("modulo.html", titulo="Alertas")

