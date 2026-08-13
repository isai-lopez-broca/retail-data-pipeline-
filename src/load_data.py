import os
from pathlib import Path

import pandas as pd
import psycopg
from dotenv import load_dotenv


# Cargar variables del archivo .env
load_dotenv()


# Conectarnos a PostgreSQL
connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)


print("Conexión exitosa a PostgreSQL.")


# Leer el CSV
ruta_clientes = Path("data/raw/clientes.csv")

df_clientes = pd.read_csv(ruta_clientes)


print("\nDatos encontrados en clientes.csv:")
print(df_clientes)


# Insertar los datos en PostgreSQL
with connection.cursor() as cursor:

    for _, fila in df_clientes.iterrows():

        cursor.execute(
            """
            INSERT INTO clientes (
                id_cliente,
                nombre,
                ciudad,
                edad
            )
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id_cliente)
            DO NOTHING
            """,
            (
                fila["id_cliente"],
                fila["nombre"],
                fila["ciudad"],
                fila["edad"]
            )
        )


# Confirmar los cambios
connection.commit()


print("\nClientes cargados correctamente.")


# Leer productos
ruta_productos = Path("data/raw/productos.csv")

df_productos = pd.read_csv(ruta_productos)

print("\nDatos encontrados en productos.csv:")
print(df_productos)


# Insertar productos en PostgreSQL
with connection.cursor() as cursor:

    for _, fila in df_productos.iterrows():

        cursor.execute(
            """
            INSERT INTO productos (
                id_producto,
                nombre,
                categoria,
                precio,
                stock
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id_producto)
            DO NOTHING
            """,
            (
                fila["id_producto"],
                fila["nombre"],
                fila["categoria"],
                fila["precio"],
                fila["stock"]
            )
        )


connection.commit()

print("\nProductos cargados correctamente.")


# Leer ventas
ruta_ventas = Path("data/raw/ventas.csv")

df_ventas = pd.read_csv(ruta_ventas)

print("\nDatos encontrados en ventas.csv:")
print(df_ventas)


# Insertar ventas en PostgreSQL
with connection.cursor() as cursor:

    for _, fila in df_ventas.iterrows():

        cursor.execute(
            """
            INSERT INTO ventas (
                id_venta,
                id_cliente,
                id_producto,
                cantidad,
                fecha
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id_venta)
            DO NOTHING
            """,
            (
                fila["id_venta"],
                fila["id_cliente"],
                fila["id_producto"],
                fila["cantidad"],
                fila["fecha"]
            )
        )


connection.commit()

print("\nVentas cargadas correctamente.")

# Cerrar conexión
connection.close()   