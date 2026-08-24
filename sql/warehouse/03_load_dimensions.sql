-- ============================================================
-- CARGA DE DIM_CLIENTE
-- ============================================================

INSERT INTO dim_cliente (
    id_cliente,
    nombre,
    ciudad,
    edad
)
SELECT
    c.id_cliente,
    c.nombre,
    c.ciudad,
    c.edad
FROM clientes c
WHERE NOT EXISTS (
    SELECT 1
    FROM dim_cliente dc
    WHERE dc.id_cliente = c.id_cliente
);


-- ============================================================
-- CARGA DE DIM_PRODUCTO
-- ============================================================

INSERT INTO dim_producto (
    id_producto,
    nombre,
    categoria,
    precio,
    stock
)
SELECT
    p.id_producto,
    p.nombre,
    p.categoria,
    p.precio,
    p.stock
FROM productos p
WHERE NOT EXISTS (
    SELECT 1
    FROM dim_producto dp
    WHERE dp.id_producto = p.id_producto
);


-- ============================================================
-- CARGA DE DIM_FECHA
-- ============================================================

INSERT INTO dim_fecha (
    fecha_key,
    fecha,
    anio,
    mes,
    nombre_mes,
    dia,
    dia_semana
)
SELECT DISTINCT
    CAST(TO_CHAR(v.fecha, 'YYYYMMDD') AS INT) AS fecha_key,
    v.fecha,
    EXTRACT(YEAR FROM v.fecha)::INT AS anio,
    EXTRACT(MONTH FROM v.fecha)::INT AS mes,
    TRIM(TO_CHAR(v.fecha, 'Month')) AS nombre_mes,
    EXTRACT(DAY FROM v.fecha)::INT AS dia,
    TRIM(TO_CHAR(v.fecha, 'Day')) AS dia_semana
FROM ventas v
WHERE NOT EXISTS (
    SELECT 1
    FROM dim_fecha df
    WHERE df.fecha_key =
          CAST(TO_CHAR(v.fecha, 'YYYYMMDD') AS INT)
); 

