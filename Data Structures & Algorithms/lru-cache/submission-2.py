class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove(self, node):
        p = node.prev
        p.next = node.next
        n = node.next
        n.prev = node.prev
    def insert(self, node):
        p = self.tail.prev
        node.next = self.tail
        node.prev = p
        self.tail.prev = node
        p.next = node
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            if len(self.cache)+1 <= self.capacity:
                self.cache[key] = node
                self.insert(node)
            else:
                first = self.head.next
                self.remove(first)
                del self.cache[first.key]
                self.insert(node)
                self.cache[key] = node



