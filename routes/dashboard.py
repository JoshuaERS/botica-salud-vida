from flask import Blueprint, render_template

from models.alerta import listar_proximos_a_vencer, listar_stock_bajo
from models.producto import listar_productos

bp = Blueprint("dashboard", __name__)


@bp.get("/")
def index():
    return render_template(
        "dashboard.html",
        total_productos=len(listar_productos()),
        total_stock_bajo=len(listar_stock_bajo()),
        total_vencimientos=len(listar_proximos_a_vencer()),
    )

