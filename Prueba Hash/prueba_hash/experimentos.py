# -*- coding: utf-8 -*-
"""
Funciones modulares para pruebas experimentales con HashTable.
Cada función exporta los resultados obtenidos a un archivo CSV con el nombre adecuado.

Variables exportadas:
- n_elements: Cantidad de elementos insertados (define la carga).
- table_size: Tamaño de la tabla hash (slots/buckets).
- factor_carga: n_elements/table_size, indica el nivel de llenado de la tabla.
- insert_time, search_time, delete_time: Tiempo de ejecución de cada operación (segundos).
- memory_usage: Uso máximo de memoria durante la inserción (MB).
- Para experimentos repetidos: promedios y desviaciones estándar de los tiempos/memoria.
"""

import random
import time
import statistics
import csv
import os
from hash import HashTable
from memoria import profile_memory_insert

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_separator():
    print("=" * 60)

def print_section(title):
    print_separator()
    print(f"{title.center(60)}")
    print_separator()

def print_kv_row(label, value, unit=None, width=30):
    val_str = f"{value:.6f}" if isinstance(value, float) else str(value)
    unit_str = f" {unit}" if unit else ""
    print(f"{label:<{width}}: {val_str}{unit_str}")

def test_hash_table(n_elements, n_search, n_delete, table_size, percent_non_existing=0.5):
    """
    Realiza inserciones, búsquedas y eliminaciones sobre la tabla hash.
    Devuelve los tiempos de ejecución de cada operación.
    """
    ht = HashTable(table_size)
    # Genera claves aleatorias y claves no existentes
    keys = [random.randint(0, 10 * n_elements) for _ in range(n_elements)]
    non_existing_keys = [max(keys) + 1 + i for i in range(max(n_search, n_delete))]
    # Inserción
    t0 = time.perf_counter()
    for k in keys:
        ht.insert(k, str(k))
    t1 = time.perf_counter()
    insert_time = t1 - t0
    # Búsqueda (mitad existentes, mitad no existentes)
    t0 = time.perf_counter()
    for i in range(n_search):
        key = non_existing_keys[i] if i < int(n_search * percent_non_existing) else random.choice(keys)
        ht.search(key)
    t1 = time.perf_counter()
    search_time = t1 - t0
    # Eliminación (mitad existentes, mitad no existentes)
    t0 = time.perf_counter()
    for i in range(n_delete):
        key = non_existing_keys[i] if i < int(n_delete * percent_non_existing) else random.choice(keys)
        ht.delete(key)
    t1 = time.perf_counter()
    delete_time = t1 - t0
    return insert_time, search_time, delete_time

def prueba_personalizada_export():
    """
    Ejecuta una sola prueba personalizada e **exporta** el detalle a 'personalizada_hash.csv'.
    Muestra resumen en pantalla y tiempo total de ejecución.
    """
    clear_screen()
    print_section("PRUEBA PERSONALIZADA CON EXPORTACIÓN")
    total_t0 = time.perf_counter()
    n = int(input("Ingrese cantidad de elementos: "))
    m = int(input("Ingrese tamaño de la tabla hash: "))
    b = int(input("Número de búsquedas: "))
    e = int(input("Número de eliminaciones: "))
    print("\nEjecutando prueba, por favor espere...\n")
    ins, bus, elim = test_hash_table(n, b, e, m)
    mem = profile_memory_insert(n, m)
    total_t1 = time.perf_counter()
    row = {
        'n_elements': n,
        'table_size': m,
        'factor_carga': round(n / m, 2),
        'insert_time': ins,
        'search_time': bus,
        'delete_time': elim,
        'memory_usage': mem,
        'total_exec_time': total_t1 - total_t0
    }
    filename = 'personalizada_hash.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writeheader()
        writer.writerow(row)
    print_section("RESUMEN DE LA PRUEBA")
    print_kv_row("Elementos insertados", n)
    print_kv_row("Tamaño de la tabla", m)
    print_kv_row("Factor de carga", row['factor_carga'])
    print_kv_row("Tiempo de inserción", ins, "s")
    print_kv_row("Tiempo de búsqueda", bus, "s")
    print_kv_row("Tiempo de eliminación", elim, "s")
    print_kv_row("Uso máx. de memoria", mem, "MB")
    print_kv_row("Tiempo total de ejecución", row['total_exec_time'], "s")
    print_separator()
    print(f"\n¡Resultados exportados a {filename}!\n")

def perfil_memoria_simple_export():
    """
    Mide el uso de memoria para una inserción y **exporta** el resultado a 'memoria_hash.csv'.
    Muestra resumen en pantalla y tiempo total de ejecución.
    """
    clear_screen()
    print_section("PERFILADO DE MEMORIA SIMPLE CON EXPORTACIÓN")
    total_t0 = time.perf_counter()
    n = int(input("Ingrese cantidad de elementos: "))
    m = int(input("Ingrese tamaño de la tabla hash: "))
    print("\nEjecutando perfilado de memoria, por favor espere...\n")
    uso = profile_memory_insert(n, m)
    total_t1 = time.perf_counter()
    row = {
        'n_elements': n,
        'table_size': m,
        'factor_carga': round(n / m, 2),
        'memory_usage': uso,
        'total_exec_time': total_t1 - total_t0
    }
    filename = 'memoria_hash.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writeheader()
        writer.writerow(row)
    print_section("RESUMEN DEL PERFIL DE MEMORIA")
    print_kv_row("Elementos insertados", n)
    print_kv_row("Tamaño de la tabla", m)
    print_kv_row("Factor de carga", row['factor_carga'])
    print_kv_row("Uso máx. de memoria", uso, "MB")
    print_kv_row("Tiempo total de ejecución", row['total_exec_time'], "s")
    print_separator()
    print(f"\n¡Resultados exportados a {filename}!\n")

def run_experiments_export(
    sizes=[1000, 5000, 10000],
    table_sizes=[1000, 2000, 5000],
    n_search=1000,
    n_delete=1000,
    repetitions=10,
    csv_filename='resultados_hash.csv'
):
    """
    Ejecuta experimentos repetidos para cada combinación de n_elements y table_size.
    Exporta promedios y desviaciones estándar a CSV y muestra resumen.
    """
    clear_screen()
    print_section("EXPERIMENTO COMPLETO CON REPETICIONES Y EXPORTACIÓN")
    total_t0 = time.perf_counter()
    results = []
    for n_elements in sizes:
        for table_size in table_sizes:
            factor_carga = n_elements / table_size
            insert_times, search_times, delete_times, mem_usages = [], [], [], []
            for i in range(repetitions):
                print(f"Prueba {i+1}/{repetitions} - n={n_elements}, tabla={table_size}, α={factor_carga:.2f}")
                ins_t, sch_t, del_t = test_hash_table(
                    n_elements, n_search, n_delete, table_size, percent_non_existing=0.5
                )
                insert_times.append(ins_t)
                search_times.append(sch_t)
                delete_times.append(del_t)
                mem_usages.append(profile_memory_insert(n_elements, table_size))
            results.append({
                'n_elements': n_elements,
                'table_size': table_size,
                'factor_carga': round(factor_carga, 2),
                'insert_time_avg': statistics.mean(insert_times),
                'insert_time_std': statistics.stdev(insert_times) if len(insert_times) > 1 else 0.0,
                'search_time_avg': statistics.mean(search_times),
                'search_time_std': statistics.stdev(search_times) if len(search_times) > 1 else 0.0,
                'delete_time_avg': statistics.mean(delete_times),
                'delete_time_std': statistics.stdev(delete_times) if len(delete_times) > 1 else 0.0,
                'memory_usage_avg': statistics.mean(mem_usages),
                'memory_usage_std': statistics.stdev(mem_usages) if len(mem_usages) > 1 else 0.0,
            })
            print("... Listo.")
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[
            'n_elements', 'table_size', 'factor_carga',
            'insert_time_avg', 'insert_time_std',
            'search_time_avg', 'search_time_std',
            'delete_time_avg', 'delete_time_std',
            'memory_usage_avg', 'memory_usage_std'
        ])
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    total_t1 = time.perf_counter()
    print_section("RESUMEN DEL EXPERIMENTO")
    print_kv_row("Configuraciones ejecutadas", len(results))
    print_kv_row("Repeticiones por configuración", repetitions)
    print_kv_row("Tiempo total de ejecución", total_t1 - total_t0, "s")
    print_separator()
    print(f"\n¡Resultados exportados a {csv_filename}!\n")
