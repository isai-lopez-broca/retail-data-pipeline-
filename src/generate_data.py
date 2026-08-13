import pandas as pd
from pathlib import Path

from generators.clientes import generar_clientes
from generators.productos import generar_productos
from generators.ventas import generar_ventas

# Clientes
clientes = generar_clientes()
df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv(Path("data/raw/clientes.csv"), index=False)

# Productos
productos = generar_productos()
df_productos = pd.DataFrame(productos)
df_productos.to_csv(Path("data/raw/productos.csv"), index=False)

# Ventas
ventas = generar_ventas()
df_ventas = pd.DataFrame(ventas)
df_ventas.to_csv(Path("data/raw/ventas.csv"), index=False)

print("Archivos generados correctamente.") 