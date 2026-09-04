import pandas as pd

from src.validate_data import validate_clientes


def test_clientes_validos():
    df = pd.DataFrame({
        "id_cliente": [1, 2],
        "nombre": ["Ana", "Luis"],
        "edad": [28, 35],
    })

    errors = validate_clientes(df)

    assert errors == []


def test_detecta_id_cliente_nulo():
    df = pd.DataFrame({
        "id_cliente": [1, None],
        "nombre": ["Ana", "Luis"],
        "edad": [28, 35],
    })

    errors = validate_clientes(df)

    assert "Existen clientes sin id_cliente." in errors


def test_detecta_edad_negativa():
    df = pd.DataFrame({
        "id_cliente": [1, 2],
        "nombre": ["Ana", "Luis"],
        "edad": [28, -5],
    })

    errors = validate_clientes(df)

    assert "Existen clientes con edad negativa." in errors


def test_detecta_ids_duplicados():
    df = pd.DataFrame({
        "id_cliente": [1, 1],
        "nombre": ["Ana", "Luis"],
        "edad": [28, 35],
    })

    errors = validate_clientes(df)

    assert "Existen id_cliente duplicados." in errors 