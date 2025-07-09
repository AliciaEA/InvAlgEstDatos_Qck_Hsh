# hash.py
"""
Estructura de datos HashTable con encadenamiento separado.
Contiene las clases Node (nodo de lista enlazada) y HashTable para inserción, búsqueda y eliminación eficiente.
"""

class Node:
    """Nodo simple para lista enlazada, usado en colisiones de la tabla hash."""
    def __init__(self, key, value):
        self.key = key # Clave del nodo 
        self.value = value # Valor asociado a la clave
        self.next = None # Referencia al siguiente nodo en la lista enlazada
class HashTable:
    """
    Tabla hash con encadenamiento separado.
    - size: número de slots/buckets
    - table: lista de referencias a la cabeza de cada lista enlazada
    """
    def __init__(self, size):
        self.size = size # Tamaño de la tabla hash
        self.table = [None] * size # Inicializa la tabla con None en cada slot

    def hash_function(self, key):
        """Devuelve el índice hash de la clave."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Inserta o actualiza un par clave-valor."""
        idx = self.hash_function(key)
        node = self.table[idx]
        # Recorre la lista enlazada para ver si la clave ya existe
        while node:
            if node.key == key: # Si la clave ya existe, actualiza el valor
                node.value = value # Actualiza el valor y sale
                return
            node = node.next
        new_node = Node(key, value) # Crea un nuevo nodo si la clave no existe 
        new_node.next = self.table[idx] # Inserta el nuevo nodo al inicio de la lista enlazada
        self.table[idx] = new_node

    def search(self, key):
        """Devuelve el valor de la clave o None si no existe."""
        idx = self.hash_function(key)
        node = self.table[idx]
        while node: # Recorre la lista enlazada en busca de la clave
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        """Elimina el nodo con la clave dada; True si lo elimina, False si no existe."""
        idx = self.hash_function(key)
        node = self.table[idx]
        prev = None
        while node: # Recorre la lista enlazada para encontrar el nodo a eliminar
            if node.key == key:
                if prev:
                    prev.next = node.next # Si no es el primer nodo, enlaza el nodo previo con el siguiente
                else:
                    self.table[idx] = node.next # Si es el primer nodo, actualiza la cabeza de la lista enlazada
                return True
            prev = node
            node = node.next
        return False
