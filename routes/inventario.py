from datetime import date

from flask import Blueprint, flash, redirect, render_template, request, url_for

from models.movimiento import (
    listar_lotes,
    listar_movimientos,
    registrar_entrada,
    registrar_salida,
)
from models.producto import listar_productos

bp = Blueprint("inventario", __name__, url_prefix="/inventario")


@bp.get("/")
def index():
    return render_template(
        "inventario/index.html",
        movimientos=listar_movimientos(),
        lotes=listar_lotes(),
    )


@bp.route("/entrada", methods=("GET", "POST"))
def entrada():
    if request.method == "POST":
        try:
            producto_id = int(request.form["producto_id"])
            cantidad = int(request.form["cantidad"])
            codigo = request.form["codigo_lote"].strip()
            vencimiento = date.fromisoformat(request.form["fecha_vencimiento"])
            if cantidad <= 0 or not codigo:
                raise ValueError
        except (KeyError, ValueError):
            flash("Ingrese datos válidos para la entrada.", "error")
        else:
            registrar_entrada(
                producto_id,
                codigo,
                vencimiento.isoformat(),
                cantidad,
                request.form.get("observacion", "").strip(),
            )
            flash("Entrada registrada correctamente.", "success")
            return redirect(url_for("inventario.index"))
    return render_template("inventario/entrada.html", productos=listar_productos())


@bp.route("/salida", methods=("GET", "POST"))
def salida():
    if request.method == "POST":
        try:
            lote_id = int(request.form["lote_id"])
            cantidad = int(request.form["cantidad"])
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero.")
            registrar_salida(
                lote_id, cantidad, request.form.get("observacion", "").strip()
            )
        except (KeyError, ValueError) as error:
            flash(str(error) or "Ingrese datos válidos para la salida.", "error")
        else:
            flash("Salida registrada correctamente.", "success")
            return redirect(url_for("inventario.index"))
    return render_template("inventario/salida.html", lotes=listar_lotes())

