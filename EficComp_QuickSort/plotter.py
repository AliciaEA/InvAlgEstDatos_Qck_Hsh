import matplotlib.pyplot as plt

def plot_performance(results, title="Quicksort Performance"):
    """
    Genera graficos de tiempo de ejecucion y uso de memoria.
    """
    
    sizes = sorted(results.keys())
    # Usar la clave correcta para los tiempos
    times = [results[size]['average_time'] if 'average_time' in results[size] else results[size].get('average_time_seconds', 0) for size in sizes]
    
    memories = [results[size]['peak_memory_mib'] for size in sizes if results[size]['peak_memory_mib'] is not None and results[size]['peak_memory_mib'] > 0]
    sizes_for_memory = [size for size in sizes if results[size]['peak_memory_mib'] is not None and results[size]['peak_memory_mib'] > 0] 
    
    # Filtrar para evitar ceros o negativos en log
    sizes_log = [s for s, t in zip(sizes, times) if s > 0 and t > 0]
    times_log = [t for s, t in zip(sizes, times) if s > 0 and t > 0]
    
    #Grafico de Tiempo de Ejecucion vs. Tamaño de Datos
    if sizes_log and times_log:
        plt.figure(figsize=(10, 5))
        plt.plot(sizes_log, times_log, marker='o', linestyle='-', color='blue')
        plt.xscale('log') # Escala logaritmica para N
        plt.yscale('log') # Escala logaritmica para tiempo
        plt.title(f"{title} - Tiempo de Ejecución vs. Tamaño de Datos")
        plt.xlabel("Tamaño de Datos (N)")
        plt.ylabel("Tiempo Promedio (s)")
        plt.grid(True, which='both', linestyle='--')
        plt.tight_layout()
        plt.show()
    else:
        print("No hay datos positivos para graficar tiempo en escala logarítmica.")
    
    #Grafico de Uso de Memoria vs. Tamaño de Datos
    if memories and all(m > 0 for m in memories):
        plt.figure(figsize=(10, 5))
        plt.plot(sizes_for_memory, memories, marker='o', linestyle='-', color='red')
        plt.xscale('log') # Escala logaritmica para N
        plt.title(f"{title} - Uso de Memoria vs. Tamaño de Datos")
        plt.xlabel("Tamaño de Datos (N)")
        plt.ylabel("Uso de Memoria Pico (MiB)")
        plt.grid(True, which='both', linestyle='--')
        plt.tight_layout()
        plt.show()
    else:
        print("No hay datos positivos para graficar memoria en escala logarítmica.")