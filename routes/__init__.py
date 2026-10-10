from .alertas import bp as alertas_bp
from .auth import bp as auth_bp
from .categorias import bp as categorias_bp
from .dashboard import bp as dashboard_bp
from .inventario import bp as inventario_bp
from .productos import bp as productos_bp
from .reportes import bp as reportes_bp


def register_blueprints(app):
    for blueprint in (
        dashboard_bp,
        auth_bp,
        productos_bp,
        categorias_bp,
        inventario_bp,
        alertas_bp,
        reportes_bp,
    ):
        app.register_blueprint(blueprint)

