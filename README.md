# Botica Salud & Vida

Sistema web base para gestionar productos, categorías, movimientos de inventario,
alertas y reportes de una botica. Está construido con Flask y SQLite.

## Requisitos

- Python 3.10 o superior
- Git

## Puesta en marcha

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app run --debug
```

Visite `http://127.0.0.1:5000`. La base de datos `database.db` se crea al
primer arranque a partir de `database/schema.sql`.

## Estructura

- `models/`: conexión y acceso a datos.
- `routes/`: rutas agrupadas por módulo mediante blueprints.
- `templates/`: vistas HTML con Jinja.
- `static/`: estilos, JavaScript, imágenes e iconos.
- `database/schema.sql`: definición inicial de SQLite.
- `docs/`: documentación, diagramas y entregables.
- `uploads/`: archivos cargados; su contenido no se versiona.

## Flujo Git

- `main`: versión estable.
- `develop`: integración del desarrollo.
- `feature/*`: trabajo aislado por módulo.

Ramas iniciales: `feature/login`, `feature/dashboard`, `feature/productos`,
`feature/categorias`, `feature/inventario`, `feature/alertas` y
`feature/reportes`.

## Próximos pasos

1. Reemplazar la clave secreta con una variable de entorno.
2. Implementar autenticación y autorización.
3. Completar operaciones CRUD y validaciones.
4. Añadir pruebas automatizadas.

