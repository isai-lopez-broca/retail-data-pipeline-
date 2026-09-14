import pandas as pd

from src.validate_data import (
    validate_clientes,
    validate_productos,
    validate_ventas,
    validate_integrity,
    validate_all,
) 

def test_clientes_validos():
    df = pd.DataFrame({
        "id_cliente": [1, 2],
        "nombre": ["Ana", "Luis"],
        "ciudad": ["Cancún", "Mérida"],
        "edad": [28, 35],
    })

    errors = validate_clientes(df)

    assert errors == []


def test_detecta_id_cliente_nulo():
    df = pd.DataFrame({
        "id_cliente": [1, None],
        "nombre": ["Ana", "Luis"],
        "ciudad": ["Cancún", "Mérida"],
        "edad": [28, 35],
    })

    errors = validate_clientes(df)

    assert "Existen clientes sin id_cliente." in errors


def test_detecta_edad_negativa():
    df = pd.DataFrame({
        "id_cliente": [1, 2],
        "nombre": ["Ana", "Luis"],
        "ciudad": ["Cancún", "Mérida"],
        "edad": [28, -5],
    })

    errors = validate_clientes(df)

    assert "Existen clientes con edad negativa." in errors


def test_detecta_ids_duplicados():
    df = pd.DataFrame({
        "id_cliente": [1, 1],
        "nombre": ["Ana", "Luis"],
        "ciudad": ["Cancún", "Mérida"],
        "edad": [28, 35],
    })

    errors = validate_clientes(df)

    assert "Existen id_cliente duplicados." in errors 
    
    
def test_productos_validos():
    df = pd.DataFrame({
        "id_producto": [101, 102],
        "nombre": ["Mouse Logitech", "Monitor Samsung"],
        "categoria": ["Periféricos", "Monitores"],
        "precio": [450, 4200],
        "stock": [35, 12],
    })

    errors = validate_productos(df)

    assert errors == []
    
    
def test_detecta_id_producto_nulo():
    df = pd.DataFrame({
        "id_producto": [101, None],
        "nombre": ["Mouse Logitech", "Monitor Samsung"],
        "categoria": ["Periféricos", "Monitores"],
        "precio": [450, 4200],
        "stock": [35, 12],
    })

    errors = validate_productos(df)

    assert "Existen productos sin id_producto." in errors


def test_detecta_nombre_producto_nulo():
    df = pd.DataFrame({
        "id_producto": [101, 102],
        "nombre": ["Mouse Logitech", None],
        "categoria": ["Periféricos", "Monitores"],
        "precio": [450, 4200],
        "stock": [35, 12],
    })

    errors = validate_productos(df)

    assert "Existen productos sin nombre." in errors


def test_detecta_precio_invalido():
    df = pd.DataFrame({
        "id_producto": [101, 102],
        "nombre": ["Mouse Logitech", "Monitor Samsung"],
        "categoria": ["Periféricos", "Monitores"],
        "precio": [450, 0],
        "stock": [35, 12],
    })

    errors = validate_productos(df)

    assert "Existen productos con precio inválido." in errors


def test_detecta_stock_negativo():
    df = pd.DataFrame({
        "id_producto": [101, 102],
        "nombre": ["Mouse Logitech", "Monitor Samsung"],
        "categoria": ["Periféricos", "Monitores"],
        "precio": [450, 4200],
        "stock": [35, -5],
    })

    errors = validate_productos(df)

    assert "Existen productos con stock negativo." in errors 
    
    
def test_ventas_validas():
    df = pd.DataFrame({
        "id_venta": [1, 2],
        "id_cliente": [1, 3],
        "id_producto": [101, 104],
        "cantidad": [2, 1],
        "fecha": ["2026-07-30", "2026-07-30"],
    })

    errors = validate_ventas(df)

    assert errors == []


def test_detecta_id_venta_nulo():
    df = pd.DataFrame({
        "id_venta": [1, None],
        "id_cliente": [1, 3],
        "id_producto": [101, 104],
        "cantidad": [2, 1],
        "fecha": ["2026-07-30", "2026-07-30"],
    })

    errors = validate_ventas(df)

    assert "Existen ventas sin id_venta." in errors


def test_detecta_id_cliente_venta_nulo():
    df = pd.DataFrame({
        "id_venta": [1, 2],
        "id_cliente": [1, None],
        "id_producto": [101, 104],
        "cantidad": [2, 1],
        "fecha": ["2026-07-30", "2026-07-30"],
    })

    errors = validate_ventas(df)

    assert "Existen ventas sin id_cliente." in errors


def test_detecta_id_producto_venta_nulo():
    df = pd.DataFrame({
        "id_venta": [1, 2],
        "id_cliente": [1, 3],
        "id_producto": [101, None],
        "cantidad": [2, 1],
        "fecha": ["2026-07-30", "2026-07-30"],
    })

    errors = validate_ventas(df)

    assert "Existen ventas sin id_producto." in errors


def test_detecta_cantidad_invalida():
    df = pd.DataFrame({
        "id_venta": [1, 2],
        "id_cliente": [1, 3],
        "id_producto": [101, 104],
        "cantidad": [2, 0],
        "fecha": ["2026-07-30", "2026-07-30"],
    })

    errors = validate_ventas(df)

    assert "Existen ventas con cantidad inválida." in errors


def test_detecta_id_venta_duplicado():
    df = pd.DataFrame({
        "id_venta": [1, 1],
        "id_cliente": [1, 3],
        "id_producto": [101, 104],
        "cantidad": [2, 1],
        "fecha": ["2026-07-30", "2026-07-30"],
    })

    errors = validate_ventas(df)

    assert "Existen id_venta duplicados." in errors 
    
    
def test_integridad_referencial_valida():
    df_clientes = pd.DataFrame({
        "id_cliente": [1, 2, 3],
    })

    df_productos = pd.DataFrame({
        "id_producto": [101, 102, 103, 104],
    })

    df_ventas = pd.DataFrame({
        "id_venta": [1, 2],
        "id_cliente": [1, 3],
        "id_producto": [101, 104],
    })

    errors = validate_integrity(
        df_ventas,
        df_clientes,
        df_productos,
    )

    assert errors == []
    
    
def test_detecta_cliente_inexistente():
    df_clientes = pd.DataFrame({
        "id_cliente": [1, 2, 3],
    })

    df_productos = pd.DataFrame({
        "id_producto": [101, 102, 103, 104],
    })

    df_ventas = pd.DataFrame({
        "id_venta": [1, 2],
        "id_cliente": [1, 99],
        "id_producto": [101, 104],
    })

    errors = validate_integrity(
        df_ventas,
        df_clientes,
        df_productos,
    )

    assert "Existen ventas con id_cliente inexistente." in errors 
    
def test_detecta_producto_inexistente():
    df_clientes = pd.DataFrame({
        "id_cliente": [1, 2, 3],
    })

    df_productos = pd.DataFrame({
        "id_producto": [101, 102, 103, 104],
    })

    df_ventas = pd.DataFrame({
        "id_venta": [1, 2],
        "id_cliente": [1, 3],
        "id_producto": [101, 999],
    })

    errors = validate_integrity(
        df_ventas,
        df_clientes,
        df_productos,
    )

    assert "Existen ventas con id_producto inexistente." in errors 
    

def test_validacion_completa_exitosa():
    df_clientes = pd.DataFrame({
        "id_cliente": [1, 2, 3],
        "nombre": ["Ana", "Luis", "Carlos"],
        "ciudad": ["Cancún", "Mérida", "CDMX"],
        "edad": [28, 35, 41],
    })

    df_productos = pd.DataFrame({
        "id_producto": [101, 102, 103, 104],
        "nombre": [
            "Mouse Logitech",
            "Monitor Samsung",
            "Teclado Redragon",
            "Laptop Lenovo",
        ],
        "categoria": [
            "Periféricos",
            "Monitores",
            "Periféricos",
            "Laptops",
        ],
        "precio": [450, 4200, 890, 18500],
        "stock": [35, 12, 20, 8],
    })

    df_ventas = pd.DataFrame({
        "id_venta": [1, 2, 3, 4],
        "id_cliente": [1, 3, 2, 1],
        "id_producto": [101, 104, 103, 102],
        "cantidad": [2, 1, 3, 1],
        "fecha": [
            "2026-07-30",
            "2026-07-30",
            "2026-07-29",
            "2026-07-28",
        ],
    })

    errors = validate_all(
        df_clientes,
        df_productos,
        df_ventas,
    )

    assert errors == [] 