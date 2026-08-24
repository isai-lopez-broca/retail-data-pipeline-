INSERT INTO fact_ventas (
    id_venta,
    cliente_key,
    producto_key,
    fecha_key,
    cantidad,
    precio_unitario,
    importe
)
SELECT
    v.id_venta,
    c.cliente_key,
    p.producto_key,
    f.fecha_key,
    v.cantidad,
    p.precio,
    v.cantidad * p.precio AS importe
FROM ventas v
JOIN dim_cliente c
    ON v.id_cliente = c.id_cliente
JOIN dim_producto p
    ON v.id_producto = p.id_producto
JOIN dim_fecha f
    ON v.fecha = f.fecha
ON CONFLICT (id_venta) DO NOTHING;
