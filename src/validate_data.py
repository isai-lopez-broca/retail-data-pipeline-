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

    # Validar edades negativas
    if (df["edad"] < 0).any():
        errors.append("Existen clientes con edad negativa.")

    # Validar IDs duplicados
    if df["id_cliente"].duplicated().any():
        errors.append("Existen id_cliente duplicados.")

    return errors 