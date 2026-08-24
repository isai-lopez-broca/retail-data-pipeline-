-- Dimension cliente.
CREATE TABLE IF NOT EXISTS dim_cliente (
    cliente_key SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    nombre VARCHAR(100),
    ciudad VARCHAR(100),
    edad INT
);
 
-- Dimension producto.
CREATE TABLE IF NOT EXISTS dim_producto (
    producto_key SERIAL PRIMARY KEY,
    id_producto INT NOT NULL,
    nombre VARCHAR(100),
    categoria VARCHAR(100),
    precio NUMERIC(10, 2),
    stock INT
);

-- Dimension fecha.
CREATE TABLE IF NOT EXISTS dim_fecha (
    fecha_key INT PRIMARY KEY,
    fecha DATE NOT NULL,
    anio INT,
    mes INT,
    nombre_mes VARCHAR(20),
    dia INT,
    dia_semana VARCHAR(20)
);

