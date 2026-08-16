def insert_dataframe(
    connection,
    dataframe,
    table_name,
    columns,
    conflict_column,
):
    """
    Inserta los datos de un DataFrame en PostgreSQL.
    Si el ID ya existe, no duplica el registro.
    """

    placeholders = ", ".join(["%s"] * len(columns))
    column_names = ", ".join(columns)

    query = f"""
        INSERT INTO {table_name} ({column_names})
        VALUES ({placeholders})
        ON CONFLICT ({conflict_column})
        DO NOTHING
    """

    with connection.cursor() as cursor:

        for _, row in dataframe.iterrows():

            values = tuple(row[column] for column in columns)

            cursor.execute(query, values) 