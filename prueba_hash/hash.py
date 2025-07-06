# hash.py
"""
Estructura de datos HashTable con encadenamiento separado.
Contiene las clases Node (nodo de lista enlazada) y HashTable para inserción, búsqueda y eliminación eficiente.
"""

class Node:
    """Nodo simple para lista enlazada, usado en colisiones de la tabla hash."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """
    Tabla hash con encadenamiento separado.
    - size: número de slots/buckets
    - table: lista de referencias a la cabeza de cada lista enlazada
    """
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Devuelve el índice hash de la clave."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Inserta o actualiza un par clave-valor."""
        idx = self.hash_function(key)
        node = self.table[idx]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.table[idx]
        self.table[idx] = new_node

    def search(self, key):
        """Devuelve el valor de la clave o None si no existe."""
        idx = self.hash_function(key)
        node = self.table[idx]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        """Elimina el nodo con la clave dada; True si lo elimina, False si no existe."""
        idx = self.hash_function(key)
        node = self.table[idx]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[idx] = node.next
                return True
            prev = node
            node = node.next
        return False
