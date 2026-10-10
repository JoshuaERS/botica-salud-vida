PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    rol TEXT NOT NULL DEFAULT 'empleado',
    activo INTEGER NOT NULL DEFAULT 1,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL DEFAULT 0 CHECK (precio >= 0),
    stock_minimo INTEGER NOT NULL DEFAULT 0 CHECK (stock_minimo >= 0),
    categoria_id INTEGER,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE IF NOT EXISTS lotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    codigo TEXT NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    cantidad INTEGER NOT NULL DEFAULT 0 CHECK (cantidad >= 0),
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (producto_id, codigo),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

CREATE TABLE IF NOT EXISTS movimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    lote_id INTEGER NOT NULL,
    usuario_id INTEGER,
    tipo TEXT NOT NULL CHECK (tipo IN ('entrada', 'salida', 'ajuste')),
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    observacion TEXT,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (lote_id) REFERENCES lotes(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT OR IGNORE INTO categorias (nombre, descripcion) VALUES
    ('Medicamentos', 'Productos farmacéuticos'),
    ('Cuidado personal', 'Productos de higiene y cuidado'),
    ('Primeros auxilios', 'Materiales para atención básica');

