CREATE TABLE clientes (

    id_cliente INTEGER PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    ciudad VARCHAR(100),

    edad INTEGER

);

CREATE TABLE productos (

    id_producto INTEGER PRIMARY KEY,

    nombre VARCHAR(150) NOT NULL,

    categoria VARCHAR(100),

    precio NUMERIC(10,2),

    stock INTEGER

);

CREATE TABLE ventas (

    id_venta INTEGER PRIMARY KEY,

    id_cliente INTEGER NOT NULL,

    id_producto INTEGER NOT NULL,

    cantidad INTEGER NOT NULL,

    fecha DATE NOT NULL,

    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente),

    FOREIGN KEY (id_producto)
        REFERENCES productos(id_producto)

);