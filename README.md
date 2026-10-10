# Botica Salud & Vida

Sistema web base para gestionar productos, categorías, movimientos de inventario,
alertas y reportes de una botica. Está construido con Flask y SQLite.

La versión actual permite registrar y buscar productos, controlar existencias por
lote, registrar entradas y salidas, impedir cantidades negativas y consultar
alertas de stock mínimo y vencimiento.

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

Para reiniciar los datos durante el desarrollo, cierre la aplicación, elimine
`database.db` y vuelva a iniciarla.

## Pruebas

```powershell
python -m unittest discover -s tests -v
```

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

### Trabajo en equipo

Cada integrante debe configurar su propia identidad de Git y realizar un aporte
real en una rama de funcionalidad. Ejemplo:

```powershell
git config user.name "Nombre Apellido"
git config user.email "correo-del-integrante@example.com"
git switch develop
git switch feature/productos
# Editar y comprobar los archivos asignados.
git add ruta-del-archivo
git commit -m "feat: descripción concreta del aporte"
```

Después se integra la rama mediante una revisión o solicitud de cambios. No se
deben crear commits ficticios ni compartir la misma identidad, porque el
historial debe representar la participación real de cada integrante.

La descripción técnica del primer avance se encuentra en
`docs/entregables/avance-1.md`.

## Próximos pasos

1. Reemplazar la clave secreta con una variable de entorno.
2. Implementar autenticación y autorización.
3. Completar operaciones CRUD y validaciones.
4. Añadir pruebas automatizadas.

