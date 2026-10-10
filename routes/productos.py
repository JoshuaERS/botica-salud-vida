from flask import Blueprint, flash, redirect, render_template, request, url_for

from models.categoria import listar_categorias
from models.producto import crear_producto, listar_productos

bp = Blueprint("productos", __name__, url_prefix="/productos")


@bp.get("/")
def index():
    busqueda = request.args.get("q", "")
    return render_template(
        "productos/index.html",
        productos=listar_productos(busqueda),
        busqueda=busqueda,
    )


@bp.route("/nuevo", methods=("GET", "POST"))
def nuevo():
    if request.method == "POST":
        try:
            nombre = request.form["nombre"].strip()
            precio = float(request.form["precio"])
            stock_minimo = int(request.form["stock_minimo"])
            categoria_id = int(request.form["categoria_id"])
            if not nombre or precio < 0 or stock_minimo < 0:
                raise ValueError
        except (KeyError, ValueError):
            flash("Complete los campos con valores válidos.", "error")
        else:
            crear_producto(
                nombre,
                request.form.get("descripcion", "").strip(),
                precio,
                stock_minimo,
                categoria_id,
            )
            flash("Producto registrado correctamente.", "success")
            return redirect(url_for("productos.index"))
    return render_template("productos/form.html", categorias=listar_categorias())

