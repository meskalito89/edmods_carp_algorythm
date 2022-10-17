import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hash_table:

    def __init__(self, capacity=29):
        self.holders = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def hash_funciton(self, key):
        hashsum = 0
        for index, char in enumerate(key):
            hashsum += (index + len(key))**ord(char)
        return hashsum % self.capacity

    def insert(self, key, value):
        self.size +=1
        hash_index = self.hash_funciton(key)
        node = self.holders[hash_index]

        if node is None:
            self.holders[hash_index] = Node(key, value)
            return

        while node.next is not None:
            node = node.next

        node.next = Node(key, value)

    def find(self, key):
        hash_index = self.hash_funciton(key)
        node = self.holders[hash_index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return

        if node.key == key:
            return node.value


    def remove(self, key):
        hash_index = self.hash_funciton(key)
        node = self.holders[hash_index]
        prev_node = None

        while node is not None and node.key != key:
            node = node.next
            prev_node = node

        if node is None:
            return

        else:
            if prev_node is None:
                self.holders[hash_index] = None
            else:
                prev_node.next = prev_node.next.next


ht = Hash_table()
print(ht.hash_funciton('stron'))
