# memoria.py
"""
Funciones para perfilamiento y medición de uso de memoria usando memory_profiler.
Requiere instalar memory_profiler: pip install memory_profiler
"""

from memory_profiler import memory_usage
from hash import HashTable
import random

def profile_memory_insert(n_elements, table_size):
    """
    Mide el consumo de memoria durante la inserción de n_elements en una HashTable.
    Devuelve el uso máximo en MB.
    """
    def run():
        ht = HashTable(table_size)
        keys = [random.randint(0, 10 * n_elements) for _ in range(n_elements)]
        for k in keys:
            ht.insert(k, str(k))
    mem = memory_usage(run, max_iterations=1, interval=0.01)
    return max(mem) - min(mem)
