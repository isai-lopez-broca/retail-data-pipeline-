import pandas as pd


def validate_clientes(df):
    """
    Valida los datos de clientes.
    """

    errors = []

    # Validar IDs nulos
    if df["id_cliente"].isnull().any():
        errors.append("Existen clientes sin id_cliente.")

    # Validar nombres nulos
    if df["nombre"].isnull().any():
        errors.append("Existen clientes sin nombre.")
        
    # Validar ciudades nulas
    if df["ciudad"].isnull().any():
        errors.append("Existen clientes sin ciudad.")

    # Validar edades negativas
    if (df["edad"] < 0).any():
        errors.append("Existen clientes con edad negativa.")

    # Validar IDs duplicados
    if df["id_cliente"].duplicated().any():
        errors.append("Existen id_cliente duplicados.")

    return errors 



def validate_productos(df):
    """
    Valida los datos de productos.
    """

    errors = []

    # Validar IDs nulos
    if df["id_producto"].isnull().any():
        errors.append("Existen productos sin id_producto.")

    # Validar nombres nulos
    if df["nombre"].isnull().any():
        errors.append("Existen productos sin nombre.")

    # Validar precios inválidos
    if (df["precio"] <= 0).any():
        errors.append("Existen productos con precio inválido.")

    # Validar stock negativo
    if (df["stock"] < 0).any():
        errors.append("Existen productos con stock negativo.")

    return errors


def validate_ventas(df):
    """
    Valida los datos de ventas.
    """

    errors = []

    # Validar IDs de venta nulos
    if df["id_venta"].isnull().any():
        errors.append("Existen ventas sin id_venta.")

    # Validar IDs de cliente nulos
    if df["id_cliente"].isnull().any():
        errors.append("Existen ventas sin id_cliente.")

    # Validar IDs de producto nulos
    if df["id_producto"].isnull().any():
        errors.append("Existen ventas sin id_producto.")

    # Validar cantidades inválidas
    if (df["cantidad"] <= 0).any():
        errors.append("Existen ventas con cantidad inválida.")

    # Validar fechas nulas
    if df["fecha"].isnull().any():
        errors.append("Existen ventas sin fecha.")

    # Validar IDs de venta duplicados
    if df["id_venta"].duplicated().any():
        errors.append("Existen id_venta duplicados.")

    return errors 


def validate_integrity(df_ventas, df_clientes, df_productos):
    """
    Valida la integridad referencial entre ventas,
    clientes y productos.
    """

    errors = []

    # Validar clientes existentes
    clientes_validos = set(df_clientes["id_cliente"])

    if not df_ventas["id_cliente"].isin(clientes_validos).all():
        errors.append("Existen ventas con id_cliente inexistente.")

    # Validar productos existentes
    productos_validos = set(df_productos["id_producto"])

    if not df_ventas["id_producto"].isin(productos_validos).all():
        errors.append("Existen ventas con id_producto inexistente.")

    return errors 

def validate_all(df_clientes, df_productos, df_ventas):
    """
    Ejecuta todas las validaciones de calidad e integridad.
    """

    errors = []

    errors.extend(validate_clientes(df_clientes))
    errors.extend(validate_productos(df_productos))
    errors.extend(validate_ventas(df_ventas))
    errors.extend(
        validate_integrity(
            df_ventas,
            df_clientes,
            df_productos,
        )
    )

    return errors 

if __name__ == "__main__":
    from pathlib import Path
    import pandas as pd

    BASE_DIR = Path(__file__).resolve().parent.parent

    clientes = pd.read_csv(BASE_DIR / "data" / "raw" / "clientes.csv")
    productos = pd.read_csv(BASE_DIR / "data" / "raw" / "productos.csv")
    ventas = pd.read_csv(BASE_DIR / "data" / "raw" / "ventas.csv")

    errors = validate_all(
        clientes,
        productos,
        ventas,
    )

    if errors:
        print("\n❌ ERRORES DE VALIDACIÓN:")

        for error in errors:
            print(f"- {error}")

        raise ValueError("Los datos no son válidos.")

    print("\n✅ Todos los datos pasaron las validaciones.")