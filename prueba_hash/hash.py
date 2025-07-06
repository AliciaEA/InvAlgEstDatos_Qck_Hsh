class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
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
        idx = self._hash(key)
        node = self.table[idx]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        idx = self._hash(key)
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
