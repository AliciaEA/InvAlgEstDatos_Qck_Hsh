# main.py
"""
Menú principal del experimento. Solo contiene la lógica del menú y las llamadas a funciones.
"""

# main.py
from experimentos import (
    prueba_personalizada_export,
    perfil_memoria_simple_export,
    run_experiments_export,
    clear_screen
)

def main_menu():
    while True:
        # Limpiar pantalla (opcional, depende del sistema operativo)
        clear_screen()
        print("\n=== Menú principal (Hash Experimental, todo se exporta) ===")
        print("1. Prueba personalizada (exporta personalizada_hash.csv)")
        print("2. Solo perfil de memoria (exporta memoria_hash.csv)")
        print("3. Experimento completo (repeticiones, exporta resultados_hash.csv)")
        print("4. Salir")
        op = input("Seleccione una opción: ")
        match op:
            case "1":
                prueba_personalizada_export()
            case "2":
                perfil_memoria_simple_export()
            case "3":
                run_experiments_export(
                    sizes=[20000,55000, 100000, 200000, 500000, 1000000],
                    table_sizes=[1000, 2000, 5000],
                    n_search=1000,
                    n_delete=1000,
                    repetitions=10,
                    csv_filename='resultados_hash.csv'
                )
            case "4":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main_menu()
