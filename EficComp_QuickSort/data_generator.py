import random


def generate_random_list(size, max_value=None):
    """Genera una lista de numeros aleatorios"""
    
    if max_value is None:
        max_value = size * 10
    return [random.randint(0, max_value) for _ in range(size)]

def generate_ordered_list(size):
    """Genera una lista ordenada de numeros"""
    
    return list(range(size))

def generate_reverse_ordered_list(size):
    """Genera una lista ordenada de numeros en orden inverso"""
    
    return list(range(size - 1, -1, -1))

def generate_duplicates_list(size, num_unique_elements=10):
    """Genera una lista con numeros duplicados"""
    
    return [random.randint(0, num_unique_elements - 1) for _ in range(size)]
 

    

