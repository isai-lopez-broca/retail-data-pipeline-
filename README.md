# Retail Data Pipeline

Pipeline de datos desarrollado con **Python, Pandas, PostgreSQL, SQL, Pytest y GitHub Actions**.

El proyecto simula un flujo completo de ingeniería de datos: recibe información de clientes, productos y ventas en archivos CSV, valida su calidad e integridad, carga los datos en PostgreSQL, construye un **Data Warehouse dimensional** y permite realizar consultas analíticas mediante SQL.

---

## 🎯 Objetivo

Construir un pipeline de datos reproducible que cubra diferentes etapas de un proceso de ingeniería de datos:

```text
CSV
 ↓
Python + Pandas
 ↓
Data Quality
 ↓
PostgreSQL
 ↓
Data Warehouse
 ↓
SQL Analytics
 ↓
Pytest
 ↓
GitHub Actions
```

El proyecto fue construido como práctica para desarrollar habilidades relacionadas con un perfil de **Data Engineer Jr**.

---

## 🏗️ Arquitectura

El flujo principal del proyecto es:

```text
                 ┌──────────────────┐
                 │   Archivos CSV   │
                 │                  │
                 │ clientes.csv     │
                 │ productos.csv    │
                 │ ventas.csv       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Python + Pandas  │
                 │                  │
                 │ Lectura de datos │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Data Quality    │
                 │                  │
                 │ Validaciones     │
                 │ Integridad       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   PostgreSQL     │
                 │                  │
                 │ clientes         │
                 │ productos        │
                 │ ventas           │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Data Warehouse  │
                 │                  │
                 │ dim_cliente      │
                 │ dim_producto     │
                 │ dim_fecha        │
                 │ fact_ventas      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  SQL Analytics   │
                 │                  │
                 │ Ventas           │
                 │ Clientes         │
                 │ Productos        │
                 │ Rankings         │
                 └──────────────────┘

                          │
                          ▼
                 ┌──────────────────┐
                 │      Pytest      │
                 │                  │
                 │ 19 tests         │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ GitHub Actions   │
                 │                  │
                 │ Continuous       │
                 │ Integration      │
                 └──────────────────┘
```

---

## 📂 Estructura del proyecto

```text
retail-data-pipeline/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   └── raw/
│       ├── clientes.csv
│       ├── productos.csv
│       └── ventas.csv
│
├── sql/
│   ├── create_tables.sql
│   ├── queries.sql
│   │
│   └── warehouse/
│       ├── 01_create_dimensions.sql
│       ├── 02_create_fact.sql
│       ├── 03_load_dimensions.sql
│       └── 04_load_fact.sql
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── generate_data.py
│   ├── load_data.py
│   ├── pipeline.py
│   ├── run_warehouse.py
│   ├── utils.py
│   ├── validate_data.py
│   │
│   └── generators/
│       ├── clientes.py
│       ├── productos.py
│       └── ventas.py
│
├── tests/
│   └── test_validate_data.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📥 Datos de entrada

El pipeline trabaja con tres archivos CSV:

### Clientes

```text
id_cliente,nombre,ciudad,edad
```

Contiene información básica de los clientes.

### Productos

```text
id_producto,nombre,categoria,precio,stock
```

Contiene información de los productos disponibles.

### Ventas

```text
id_venta,id_cliente,id_producto,cantidad,fecha
```

Contiene las transacciones realizadas.

Los archivos ubicados en `data/raw/` corresponden a datos de práctica utilizados para demostrar el funcionamiento del pipeline.

---

## 🐍 Python y Pandas

Python se utiliza para controlar el flujo del pipeline y ejecutar las diferentes etapas.

Pandas se utiliza principalmente para:

* Leer archivos CSV.
* Trabajar con DataFrames.
* Validar información.
* Preparar los datos antes de cargarlos en PostgreSQL.

El proyecto centraliza la conexión a PostgreSQL mediante:

```text
src/database.py
```

Esto evita duplicar la lógica de conexión en diferentes scripts.

---

## 🔍 Data Quality

Antes de cargar los datos en PostgreSQL, el pipeline ejecuta diferentes validaciones.

Las validaciones incluyen:

### Clientes

* IDs nulos.
* Nombres nulos.
* Ciudades nulas.
* Edades negativas.
* IDs duplicados.

### Productos

* IDs nulos.
* Nombres nulos.
* Precios inválidos.
* Stock negativo.

### Ventas

* IDs de venta nulos.
* IDs de cliente nulos.
* IDs de producto nulos.
* Cantidades inválidas.
* Fechas nulas.
* IDs de venta duplicados.

### Integridad referencial

También se verifica que:

* Cada `id_cliente` utilizado en una venta exista en `clientes`.
* Cada `id_producto` utilizado en una venta exista en `productos`.

Si alguna validación falla, el pipeline se detiene y los datos no continúan hacia las siguientes etapas.

---

## 🐘 PostgreSQL

PostgreSQL funciona como sistema de almacenamiento principal.

El modelo operacional contiene tres tablas:

```text
clientes
productos
ventas
```

Las relaciones principales son:

```text
clientes
   │
   └──── id_cliente
              │
              ▼
           ventas
              │
              └──── id_producto
                         │
                         ▼
                     productos
```

Las tablas se crean mediante:

```text
sql/create_tables.sql
```

---

## 🏢 Data Warehouse

El proyecto también implementa un pequeño **Data Warehouse dimensional**.

El modelo está compuesto por:

### Dimensiones

```text
dim_cliente
dim_producto
dim_fecha
```

### Tabla de hechos

```text
fact_ventas
```

La tabla `fact_ventas` contiene métricas relacionadas con las ventas:

* Cantidad.
* Precio unitario.
* Importe.

Y mantiene relaciones con las dimensiones correspondientes.

Conceptualmente:

```text
                 dim_cliente
                      │
                      │
                      ▼
dim_producto ───► fact_ventas ◄─── dim_fecha
```

---

## 🔄 Idempotencia

El pipeline fue diseñado para evitar insertar registros duplicados cuando se ejecuta nuevamente.

En las cargas se utilizan mecanismos como:

```sql
ON CONFLICT DO NOTHING
```

y verificaciones mediante:

```sql
WHERE NOT EXISTS
```

La idempotencia fue comprobada ejecutando el pipeline múltiples veces y verificando que los registros de `fact_ventas` no se duplicaran.

---

## 📊 SQL Analytics

El archivo:

```text
sql/queries.sql
```

contiene consultas para analizar los datos.

Entre ellas:

* Ventas con información de clientes y productos.
* Ventas totales.
* Total gastado por cliente.
* Ingresos por producto.
* Cantidad de ventas por cliente.
* Unidades vendidas.
* Precio promedio.
* Clientes que superan determinado gasto.
* Ranking de clientes.

También se utilizan conceptos de SQL como:

* `JOIN`
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* `SUM`
* `AVG`
* `COUNT`
* `WITH`
* CTEs
* Funciones de ventana
* `RANK()`

---

## 🧪 Pruebas

El proyecto utiliza **Pytest** para comprobar el comportamiento de las validaciones.

Actualmente cuenta con:

```text
19 tests
19 passed
```

Las pruebas cubren diferentes escenarios válidos e inválidos para:

* Clientes.
* Productos.
* Ventas.
* Integridad referencial.
* Validación completa.

Para ejecutar las pruebas:

```bash
python -m pytest
```

---

## ⚙️ GitHub Actions

El proyecto utiliza **GitHub Actions** para ejecutar automáticamente las pruebas.

Workflow:

```text
.github/workflows/ci.yml
```

El proceso realiza:

```text
Checkout del repositorio
        ↓
Configuración de Python 3.12
        ↓
Instalación de dependencias
        ↓
Ejecución de Pytest
```

Esto permite detectar errores automáticamente cuando se realizan cambios mediante `push` o `pull request`.

---

## 🔐 Variables de entorno

Las credenciales y configuración de PostgreSQL se almacenan mediante variables de entorno.

El proyecto utiliza un archivo:

```text
.env
```

con variables como:

```text
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

El archivo `.env` está incluido en `.gitignore` para evitar subir credenciales al repositorio.

---

## ▶️ Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/isai-lopez-broca/retail-data-pipeline-.git
```

Entrar al proyecto:

```bash
cd retail-data-pipeline-
```

### 2. Crear entorno virtual

```bash
python3 -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

Crear las variables de entorno necesarias en `.env`:

```text
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=...
```

### 5. Crear las tablas operacionales

Ejecutar:

```text
sql/create_tables.sql
```

### 6. Ejecutar el pipeline

Desde la raíz del proyecto:

```bash
python src/pipeline.py
```

El pipeline ejecutará:

```text
1. Validación de datos
        ↓
2. Carga a PostgreSQL
        ↓
3. Actualización del Data Warehouse
```

Si todos los pasos terminan correctamente se mostrará:

```text
🎉 PIPELINE COMPLETADO CORRECTAMENTE
```

---

## 🧪 Ejecutar solamente las validaciones

También es posible ejecutar las validaciones directamente:

```bash
python src/validate_data.py
```

Y ejecutar los tests:

```bash
python -m pytest
```

---

## 🏭 Ejecutar solamente el Data Warehouse

Para ejecutar la construcción y carga del Warehouse:

```bash
python src/run_warehouse.py
```

Este script ejecuta:

```text
01_create_dimensions.sql
02_create_fact.sql
03_load_dimensions.sql
04_load_fact.sql
```

---

## 🛠️ Tecnologías utilizadas

| Tecnología     | Uso                             |
| -------------- | ------------------------------- |
| Python         | Lógica del pipeline             |
| Pandas         | Procesamiento de datos          |
| PostgreSQL     | Base de datos                   |
| SQL            | Transformaciones y análisis     |
| Pytest         | Pruebas automatizadas           |
| Git            | Control de versiones            |
| GitHub         | Repositorio y colaboración      |
| GitHub Actions | CI                              |
| python-dotenv  | Gestión de variables de entorno |

---

## 📚 Conceptos practicados

Durante el desarrollo del proyecto se trabajaron conceptos de:

* Data Engineering.
* ETL.
* Data Quality.
* Data Validation.
* Integridad referencial.
* Python.
* Pandas.
* PostgreSQL.
* SQL.
* CTEs.
* Window Functions.
* Data Warehouse.
* Dimensiones.
* Tablas de hechos.
* Claves primarias y foráneas.
* Idempotencia.
* Testing.
* Pytest.
* Git.
* Branches.
* Pull Requests.
* GitHub Actions.
* Continuous Integration.
* Variables de entorno.
* Refactorización de código.

---

## 🚧 Mejoras futuras

El proyecto representa una implementación educativa y deliberadamente mantiene un alcance limitado.

Algunas mejoras que podrían implementarse posteriormente:

* Incorporar una fuente de datos externa o API.
* Incorporar Docker.
* Utilizar un orquestador como Airflow.
* Implementar transformaciones más complejas.
* Incorporar monitoreo y logging más avanzado.
* Implementar Slowly Changing Dimensions (SCD).
* Incorporar un almacenamiento cloud.
* Incorporar herramientas de transformación como dbt.
* Trabajar con grandes volúmenes de datos mediante Spark.

Estas tecnologías no forman parte de la implementación actual del proyecto.

---

## 📌 Estado del proyecto

### Implementado

* [x] Ingesta de datos CSV
* [x] Procesamiento con Python
* [x] Procesamiento con Pandas
* [x] Validación de datos
* [x] Validación de integridad referencial
* [x] PostgreSQL
* [x] ETL
* [x] Data Warehouse
* [x] Dimensiones
* [x] Tabla de hechos
* [x] Consultas analíticas
* [x] Idempotencia
* [x] Pytest
* [x] Git
* [x] GitHub
* [x] Pull Requests
* [x] GitHub Actions
* [x] Continuous Integration

### No implementado actualmente

* [ ] SCD
* [ ] Docker
* [ ] Airflow
* [ ] Spark
* [ ] Databricks
* [ ] Cloud
* [ ] dbt

---

## 👨‍💻 Autor

**Isai López Broca**

Proyecto desarrollado como parte del proceso de aprendizaje y preparación para un perfil de **Data Engineer Jr**.
