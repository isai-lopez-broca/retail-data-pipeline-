from pathlib import Path
from database import create_connection


# Ruta del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

SQL_DIR = BASE_DIR / "sql" / "warehouse"


# Conectar a PostgreSQL
connection = create_connection()

print("Conexión exitosa a PostgreSQL.")


# Archivos SQL que ejecutaremos
sql_files = [
    "01_create_dimensions.sql",
    "02_create_fact.sql",
    "03_load_dimensions.sql",
    "04_load_fact.sql",
]


# Ejecutar cada archivo
for sql_file in sql_files:

    sql_path = SQL_DIR / sql_file

    print(f"\nEjecutando: {sql_file}")

    sql = sql_path.read_text()

    with connection.cursor() as cursor:
        cursor.execute(sql)

    connection.commit()

    print(f"Completado: {sql_file}")


# Cerrar conexión
connection.close()

print("\nWarehouse actualizado correctamente.")

