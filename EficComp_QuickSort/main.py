import sys
import io
import re
from memory_profiler import memory_usage


from quicksort_alg import quicksort
from data_generator import generate_random_list, generate_ordered_list, generate_reverse_ordered_list, generate_duplicates_list
from performance_metrics import measure_time, calculate_average, print_results
from plotter import plot_performance

def quicksort_profiled(arr):
    return quicksort(arr)

def parse_memory_profiler_output(output_string):
    #Funcion para analizar la salida de memory_profiler
    
    for line in output_string.splitlines():
        if "MiB" in line and "Increment" not in line and "Line" not in line:
            parts = line.split()
            try:
                if "Total memory:" in line:
                    idx = parts.index("memory:") + 1
                else:
                    idx = 0
                    for i, part in enumerate(parts):
                        if "MiB" in part:
                            idx = i-1
                            break
                    if idx < 0: continue
                    
                mem_value = float(parts[idx].replace('MiB', '').strip())
                return mem_value #Retorna en MiB
            except (ValueError, IndexError):
                continue
        return None
    
def run_analysis_for_data_type(data_sizes, num_repetitions, data_generation_func, title_prefix):
    """Ejecuta el análisis para un tipo de dato específico. (Por ejemplo, lista aleatoria, ordenada, etc.)"""
    test_results = {}
    print(f"\n----Ejecutando análisis para {title_prefix}----")
    for size in data_sizes:
        print(f"\n----Probando Quicsort con {size} elementos ({title_prefix})----")
        #--- Medicion de Uso de Memoria ---
        print(f"Midiendo uso de memoria para {size} elementos ({title_prefix})...")
        data_for_memory = data_generation_func(size)  #Genera los datos segun el tipo
        mem_usage = memory_usage((quicksort_profiled, (list(data_for_memory),)), interval=0.01)
        # Calcular el pico real de memoria (diferencia máxima entre cualquier punto y el mínimo)
        if mem_usage:
            peak_memory_mib = max([m - min(mem_usage) for m in mem_usage])
        else:
            peak_memory_mib = None
        if peak_memory_mib is not None and peak_memory_mib > 0:
            print(f"Uso de memoria pico: {peak_memory_mib:.2f} MiB")
        else:
            print("No se pudo medir el uso de memoria o el valor fue 0.")
        #--- Medicion de Tiempo de Ejecucion ---
        execution_times_seconds = []
        print(f"Midiendo tiempo de ejecución para {size} elementos ({title_prefix})...")
        for i in range(num_repetitions):
            data_for_time = data_generation_func(size) #Genera los datos segun el tipo
            time_taken_seconds = measure_time(quicksort, list(data_for_time))
            execution_times_seconds.append(time_taken_seconds)
            print(f"Repetición {i+1}: {time_taken_seconds:.6f} segundos")
        average_time_seconds = calculate_average(execution_times_seconds)
        print(f"Tiempo promedio de ejecución: {average_time_seconds:.6f} segundos")
        test_results[size] = {
            'peak_memory_mib': peak_memory_mib,
            'average_time': average_time_seconds
        }
    return test_results
if __name__ == "__main__":
        print("¡El script se está ejecutando!")
        data_sizes = [100, 10000, 1000000]
        num_repetitions_per_size = 5
        
        #Ejecutar para el Caso Promedio (Aleatorio)
        
        print("----Analizando Caso Promedio (Datos Aleatorios)----")
        average_case_results = run_analysis_for_data_type(data_sizes, num_repetitions_per_size, generate_random_list, "Caso Promedio (Aleatorio)")
        
        print_results(average_case_results, "Caso Promedio (Aleatorio)")
        plot_performance(average_case_results, "QuickSort. Caso Promedio (Aleatorio)")
        
        """
         --- Ejecutar para el Peor Caso (Ordenado Ascendente) ---
    # NOTA: Para nuestra implementación de QuickSort (pivote central), una lista ya ordenada
    # NO es el peor caso. De hecho, a menudo es eficiente.
    # El verdadero peor caso para pivote central es más complejo (ej. patrón específico de medianas en sub-particiones).
    # Sin embargo, para demostrar "peor caso" para otras implementaciones de QS (pivote fijo),
    # o para ilustrar un caso "no-óptimo" para el nuestro, podemos usarlo.
        """
        
        print("----Analizando Caso Peor (Datos Ordenados)----")
        
        results_ordered_case = run_analysis_for_data_type(data_sizes, num_repetitions_per_size, generate_ordered_list, "Caso Peor (Datos Ordenados Ascendente)")
        
        print_results(results_ordered_case, "Caso Peor (Datos Ordenados Ascendente)")
        plot_performance(results_ordered_case, "QuickSort. Caso Peor (Datos Ordenados Ascendente)")
        
        #Ejecutar para el Peor Caso (Ordenado Descendente)
        print("----Analizando Caso Peor (Datos Ordenados Descendente)----")
        results_reverse_ordered_case = run_analysis_for_data_type(data_sizes, num_repetitions_per_size, generate_reverse_ordered_list, "Caso Peor (Datos Ordenados Descendente)")
        
        print_results(results_reverse_ordered_case, "Caso Peor (Datos Ordenados Descendente)")
        plot_performance(results_reverse_ordered_case, "QuickSort. Caso Peor (Datos Ordenados Descendente)")