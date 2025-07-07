import time
import pandas as pd
from memory_profiler import profile as memory_profile

def measure_time(func, *args, **kwargs):
    """
    Mide el tiempo de ejecucion de una funcion
    :param func: La función a medir.
    :param args: Argumentos posicionales para la función.
    :param kwargs: Argumentos de palabra clave para la función.
    :return: El tiempo de ejecución en segundos.
    """
    
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return (end_time - start_time) 

def calculate_average(data_points):
    """
    Calcula el promedio de una lista de puntos de datos.
    :param data_points: Lista de puntos de datos.
    :return: El promedio de los puntos de datos.
    """
    
    if not data_points:
        return 0
    return sum(data_points) / len(data_points)

def print_results(results, title="Resultados de Medición"):
    """
    Imprime los resultados en formato tabular.
    :param results: Diccionario con los resultados a imprimir.
    """
    
    print(f"\n{title}")
    data = []
    
    for size, metrics in results.items():
        row = {
            "Tamaño de Datos (N)": size,
            "Tiempo Promedio (s)":f"{metrics['average_time']:.6f}",
            "Uso de Memoria Pico (MiB)": f"{metrics['peak_memory_mib']:.2f}" if metrics['peak_memory_mib'] is not None else "N/A"
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    print("\n" + "=" * 50)