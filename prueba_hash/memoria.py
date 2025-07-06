from prueba_hash.memoria_prueba import memory_usage

def memory_test():
    ht = HashTable(size=1000)
    keys = [random_key() for _ in range(2000)]
    def fill_table():
        for k in keys:
            ht.insert(k, random.randint(1, 10000))
    mem_usage = memory_usage(fill_table, interval=0.01)
    print(f"Uso máximo de memoria: {max(mem_usage) - min(mem_usage):.2f} MB")
