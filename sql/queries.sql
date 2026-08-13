-- ==========================================
-- CONSULTAS DEL PROYECTO RETAIL DATA PIPELINE
-- ==========================================


-- 1. Ver todos los clientes

SELECT *
FROM clientes;


-- 2. Ver todos los productos

SELECT *
FROM productos;


-- 3. Ver todas las ventas

SELECT *
FROM ventas;


-- 4. Ventas con información del cliente y producto

SELECT
    v.id_venta,
    c.nombre AS cliente,
    p.nombre AS producto,
    v.cantidad,
    p.precio,
    v.cantidad * p.precio AS total,
    v.fecha
FROM ventas v
JOIN clientes c
    ON v.id_cliente = c.id_cliente
JOIN productos p
    ON v.id_producto = p.id_producto;


-- 5. Ventas totales

SELECT
    SUM(v.cantidad * p.precio) AS ventas_totales
FROM ventas v
JOIN productos p
    ON v.id_producto = p.id_producto;


-- 6. Total gastado por cliente

SELECT
    c.nombre AS cliente,
    SUM(v.cantidad * p.precio) AS total_gastado
FROM ventas v
JOIN clientes c
    ON v.id_cliente = c.id_cliente
JOIN productos p
    ON v.id_producto = p.id_producto
GROUP BY
    c.id_cliente,
    c.nombre
ORDER BY
    total_gastado DESC;


-- 7. Ingresos por producto

SELECT
    p.nombre AS producto,
    SUM(v.cantidad * p.precio) AS ingresos
FROM ventas v
JOIN productos p
    ON v.id_producto = p.id_producto
GROUP BY
    p.id_producto,
    p.nombre
ORDER BY
    ingresos DESC; 



-- ==========================================
-- CONSULTAS DE ANALISIS
-- ==========================================

-- Ventas por cliente

SELECT
    c.nombre AS cliente,
    COUNT(v.id_venta) AS cantidad_ventas
FROM ventas v
JOIN clientes c
    ON v.id_cliente = c.id_cliente
GROUP BY
    c.id_cliente,
    c.nombre
ORDER BY
    cantidad_ventas DESC;


-- Unidades vendidas

SELECT
    SUM(cantidad) AS unidades_vendidas
FROM ventas;


-- Precio promedio

SELECT
    AVG(precio) AS precio_promedio
FROM productos;


-- Ventas totales

SELECT
    SUM(v.cantidad * p.precio) AS ventas_totales
FROM ventas v
JOIN productos p
    ON v.id_producto = p.id_producto;


-- Total gastado por cliente

SELECT
    c.nombre AS cliente,
    SUM(v.cantidad * p.precio) AS total_gastado
FROM ventas v
JOIN clientes c 
    ON v.id_cliente = c.id_cliente
JOIN productos p
    ON v.id_producto = p.id_producto
GROUP BY
    c.id_cliente,
    c.nombre
ORDER BY
    total_gastado DESC;


-- Clientes que gastaron más de $10,000

SELECT
    c.nombre AS cliente,
    SUM(v.cantidad * p.precio) AS total_gastado
FROM ventas v
JOIN clientes c
    ON v.id_cliente = c.id_cliente
JOIN productos p
    ON v.id_producto = p.id_producto
GROUP BY
    c.id_cliente,
    c.nombre
HAVING
    SUM(v.cantidad * p.precio) > 10000
ORDER BY
    total_gastado DESC;


-- Ranking de clientes

WITH ventas_por_cliente AS (
    SELECT
        c.id_cliente,
        c.nombre,
        SUM(v.cantidad * p.precio) AS total_gastado
    FROM ventas v
    JOIN clientes c
        ON v.id_cliente = c.id_cliente
    JOIN productos p
        ON v.id_producto = p.id_producto
    GROUP BY
        c.id_cliente,
        c.nombre
)
SELECT
    nombre,
    total_gastado,
    RANK() OVER (
        ORDER BY total_gastado DESC
    ) AS ranking
FROM ventas_por_cliente;