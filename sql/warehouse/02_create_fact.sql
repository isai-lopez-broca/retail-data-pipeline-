CREATE TABLE IF NOT EXISTS fact_ventas (
    venta_key SERIAL PRIMARY KEY,
    id_venta INT NOT NULL,
    cliente_key INT NOT NULL,
    producto_key INT NOT NULL,
    fecha_key INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario NUMERIC(10, 2) NOT NULL,
    importe NUMERIC(12, 2) NOT NULL,

    CONSTRAINT fk_cliente
        FOREIGN KEY (cliente_key)
        REFERENCES dim_cliente(cliente_key),

    CONSTRAINT fk_producto
        FOREIGN KEY (producto_key)
        REFERENCES dim_producto(producto_key),

    CONSTRAINT fk_fecha
        FOREIGN KEY (fecha_key)
        REFERENCES dim_fecha(fecha_key)
);