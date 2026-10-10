# Avance 1 Análisis diseño estructura y base de datos

## Propósito

Este avance establece una base ejecutable para el sistema de inventario de la
botica Salud y Vida. La solución organiza el código en tres capas, define el
modelo de datos y presenta las pantallas necesarias para demostrar los flujos
prioritarios con datos simulados.

## Requisitos cubiertos

- RF01: registro de productos con categoría, precio y stock mínimo.
- RF02: consulta y búsqueda de productos registrados.
- RF03: registro de entradas y actualización de existencias por lote.
- RF04: registro de salidas y descuento de unidades.
- RF05: identificación de productos con stock igual o inferior al mínimo.
- RF06: identificación de lotes vencidos o próximos a vencer en 30 días.
- RF07: validación de campos y rechazo de salidas superiores al stock disponible.

## Pantallas preparadas

1. Panel principal con resumen de productos y alertas.
2. Lista y búsqueda de productos.
3. Formulario de registro de productos.
4. Resumen de lotes y movimientos.
5. Formulario de entrada por producto y lote.
6. Formulario de salida por lote.
7. Consulta de alertas de stock y vencimiento.

## Modelo de datos

```text
categorias 1 ---- N productos 1 ---- N lotes
                         |              |
                         |              |
                         +---- N movimientos

usuarios 1 ------------------ N movimientos
```

El stock actual de un producto se obtiene sumando las cantidades de sus lotes.
Este diseño permite que un mismo producto tenga distintas fechas de
vencimiento sin perder trazabilidad.

## Arquitectura

- Presentación: plantillas Jinja, HTML, CSS y JavaScript.
- Aplicación: Flask y blueprints para productos, inventario y alertas.
- Datos: SQLite, consultas parametrizadas y transacciones para movimientos.

## Validación realizada

Las pruebas automatizadas verifican que las páginas principales respondan, que
el flujo producto-entrada-salida actualice la cantidad y que el sistema rechace
una salida superior al stock disponible.

