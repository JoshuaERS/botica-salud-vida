from flask import Blueprint, current_app, render_template

from models.alerta import listar_proximos_a_vencer, listar_stock_bajo

bp = Blueprint("alertas", __name__, url_prefix="/alertas")


@bp.get("/")
def index():
    dias = current_app.config["DIAS_ALERTA_VENCIMIENTO"]
    return render_template(
        "alertas/index.html",
        stock_bajo=listar_stock_bajo(),
        vencimientos=listar_proximos_a_vencer(dias),
        dias=dias,
    )

