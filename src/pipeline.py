import subprocess
import sys


def run_step(description, command):
    print("\n" + "=" * 60)
    print(description)
    print("=" * 60)

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\n❌ El paso falló: {description}")
        sys.exit(result.returncode)

    print(f"\n✅ Completado: {description}")


def main():
    run_step(
        "1. VALIDANDO DATOS",
        ["python", "src/validate_data.py"]
    )

    run_step(
        "2. CARGANDO DATOS A POSTGRESQL",
        ["python", "src/load_data.py"]
    )

    run_step(
        "3. ACTUALIZANDO DATA WAREHOUSE",
        ["python", "src/run_warehouse.py"]
    )

    print("\n" + "=" * 60)
    print("🎉 PIPELINE COMPLETADO CORRECTAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    main()
    
    