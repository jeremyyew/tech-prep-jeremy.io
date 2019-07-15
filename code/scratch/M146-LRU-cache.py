'''

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''
from collections import deque

class DLL:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = None
        self.tail.next = None
        self.len = 0

    def push(self, node):
        node.next = self.head.next 
        self.head.next = node
        self.len += 1
        if self.len > self.capacity: 
            last = self.tail.next
            if last: 
                val = last.val 
                prev = last.prev
                last.delete()
                self.tail.next = prev
                return val
    
    def delete(self, node):
        node.delete()
        self.len -= 1

class DLLNode: 
    def __init__(self, val=None):
        self.prev = self.next = None
        self.val = val
    def delete(self):
        if self.prev: 
            self.prev.next = self.next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DLL(capacity)
        self.map = {}

    def get(self, key: int) -> int:
        v, node = self.map.get(key, (-1, None))
        if node: 
            self.dll.delete(node)
            self.dll.push(DLLNode(v))
        return v

    def put(self, key: int, value: int) -> None:
        mru = DLLNode(key)
        v, node = self.map.get(key, (None, None))
        if not v:
            lru = self.dll.push(mru)
            if lru: 
                self.map[lru].pop()
        else: 
            self.dll.delete(node)
            self.dll.push(mru)
        self.map[key] = value, mru


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)