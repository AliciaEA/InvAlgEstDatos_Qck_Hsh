import random
import string
import time
from memory_profiler import memory_usage
from hash import HashTable
from colorama import Fore, Style, init

init(autoreset=True)  # Inicializa colorama

def random_key(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def format_float(val, umbral=0.01):
    # Amarillo si supera umbral
    if val > umbral:
        return f"{Fore.YELLOW}{val:>10.4f}{Style.RESET_ALL}"
    else:
        return f"{val:>10.4f}"

def hash_table_test(table_size=1000, max_factor=2.0, steps=6):
    header = (
        f"{Fore.BLUE}{'Factor':^8}│{'Claves':^8}│{'Busq':^8}│{'Elim':^8}│{'Insert(ms)':^12}│"
        f"{'Busq_ex(ms)':^13}│{'Busq_no(ms)':^13}│{'Elim(ms)':^10}│{'Mem(MB)':^10}{Style.RESET_ALL}"
    )
    sep = f"{Fore.BLUE}{'─'*8}┼{'─'*8}┼{'─'*8}┼{'─'*8}┼{'─'*12}┼{'─'*13}┼{'─'*13}┼{'─'*10}┼{'─'*10}{Style.RESET_ALL}"
    print(header)
    print(sep)
    for factor in [round(f, 2) for f in [i * (max_factor/steps) for i in range(1, steps+1)]]:
        n = int(table_size * factor)
        keys = [random_key() for _ in range(n)]
        non_existing = [random_key() for _ in range(max(100, n // 10))]
        ht = HashTable(size=table_size)

        num_muestras = max(100, n // 10)
        buscados = random.sample(keys, num_muestras)
        eliminar = random.sample(keys, num_muestras)

        # Medir memoria durante inserción masiva
        def insercion_masiva():
            for k in keys:
                ht.insert(k, random.randint(1, 10000))
        mem_usada = float(memory_usage(insercion_masiva, interval=0.1, max_usage=True))


        # Medir tiempo de inserción promedio (después de haber insertado ya todos)
        t0 = time.time()
        for k in keys:
            ht.insert(k, random.randint(1, 10000))
        t_insert = (time.time() - t0) * 1000 / n

        # Medir búsqueda existentes
        t0 = time.time()
        for k in buscados:
            ht.search(k)
        t_search_exist = (time.time() - t0) * 1000 / num_muestras

        # Medir búsqueda no existentes
        t0 = time.time()
        for k in non_existing:
            ht.search(k)
        t_search_none = (time.time() - t0) * 1000 / len(non_existing)

        # Medir eliminación
        t0 = time.time()
        for k in eliminar:
            ht.delete(k)
        t_delete = (time.time() - t0) * 1000 / num_muestras

        # Formatea la fila de la tabla
        print(
            f"{factor:^8.2f}│{n:^8d}│{len(buscados):^8d}│{len(eliminar):^8d}│"
            f" {format_float(t_insert)} │"
            f" {format_float(t_search_exist)} │"
            f" {format_float(t_search_none)} │"
            f" {format_float(t_delete)}│"
            f"{Fore.GREEN}{mem_usada:>10.2f}{Style.RESET_ALL}"
        )
        print(sep)
if __name__ == "__main__":
    hash_table_test(table_size=1100000, max_factor=10.0, steps=5)

