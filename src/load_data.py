
from pathlib import Path

import pandas as pd

from database import create_connection
from utils import insert_dataframe
from validate_data import validate_all


# ==========================================
# LEER ARCHIVOS CSV
# ==========================================

ruta_clientes = Path("data/raw/clientes.csv")
ruta_productos = Path("data/raw/productos.csv")
ruta_ventas = Path("data/raw/ventas.csv")


df_clientes = pd.read_csv(ruta_clientes)
df_productos = pd.read_csv(ruta_productos)
df_ventas = pd.read_csv(ruta_ventas)


print("\nDatos encontrados en clientes.csv:")
print(df_clientes)

print("\nDatos encontrados en productos.csv:")
print(df_productos)

print("\nDatos encontrados en ventas.csv:")
print(df_ventas)


# ==========================================
# VALIDAR DATOS
# ==========================================

errors = validate_all(
    df_clientes,
    df_productos,
    df_ventas,
)


if errors:
    print("\nERRORES DE VALIDACIÓN:")

    for error in errors:
        print(f"- {error}")

    raise ValueError(
        "La carga fue detenida debido a errores de validación."
    )


print("\nValidación completada correctamente.")


# ==========================================
# CONECTAR A POSTGRESQL
# ==========================================

connection = create_connection()

print("Conexión exitosa a PostgreSQL.")


# ==========================================
# CLIENTES
# ==========================================

insert_dataframe(
    connection=connection,
    dataframe=df_clientes,
    table_name="clientes",
    columns=[
        "id_cliente",
        "nombre",
        "ciudad",
        "edad",
    ],
    conflict_column="id_cliente",
)

connection.commit()

print("\nClientes cargados correctamente.")


# ==========================================
# PRODUCTOS
# ==========================================

insert_dataframe(
    connection=connection,
    dataframe=df_productos,
    table_name="productos",
    columns=[
        "id_producto",
        "nombre",
        "categoria",
        "precio",
        "stock",
    ],
    conflict_column="id_producto",
)

connection.commit()

print("\nProductos cargados correctamente.")


# ==========================================
# VENTAS
# ==========================================

insert_dataframe(
    connection=connection,
    dataframe=df_ventas,
    table_name="ventas",
    columns=[
        "id_venta",
        "id_cliente",
        "id_producto",
        "cantidad",
        "fecha",
    ],
    conflict_column="id_venta",
)

connection.commit()

print("\nVentas cargadas correctamente.")


# ==========================================
# CERRAR CONEXIÓN
# ==========================================

connection.close()

print("\nConexión cerrada.")

