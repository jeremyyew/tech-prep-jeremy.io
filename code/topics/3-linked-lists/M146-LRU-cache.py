'''
- Use `OrderedDict` to get O(1) time insertion/deletion/lookup while maintaining FIFO order.
- In `OrderedDictCustom`, we implement the same features (the bare minimum) using a doubly linked list and dict. Simply change the `self.cache` data structure.
- `LRUCache` manipulates the cache but keeps track of the length for it, since we want to use a general-purpose `OrderedDict`. 
'''
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        # self.cache = OrderedDictCustom()
        self.len = 0

    def __remove(self, key):
        self.cache.pop(key)
        self.len -= 1

    def __add(self, key, value):
        self.cache[key] = value
        self.len += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        # print(f'\nget({key})')
        # self.cache.print()
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.__remove(key)
        self.__add(key, value)
        if self.len > self.capacity:
            self.cache.popitem(last=False)
            self.len -= 1
        # print(f'\nput({key}, {value})')
        # self.cache.print()


class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None
        self.prev = None


class OrderedDictCustom():
    '''
    Ordered-dict-like object, implemented with dict and doubly linked list. 
    O(1) lookup, insertion and deletion. 
    '''

    def __init__(self):
        self.map = {}
        self.dummy_head, self.dummy_tail = Node(), Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def __head(self):
        return self.dummy_head.next

    def __tail(self):
        return self.dummy_tail.prev

    def __skip(self, node):
        parent = node.prev
        child = node.next
        parent.next = child
        child.prev = parent

    def __push(self, node):
        head = self.__head()
        node.next = head
        head.prev = node
        self.dummy_head.next = node
        node.prev = self.dummy_head

    def popitem(self, last=True):
        if last:
            self.map.pop(self.__head().val)
            self.__skip(self.__head())
        else:
            self.map.pop(self.__tail().val)
            self.__skip(self.__tail())

    def pop(self, key):
        v, node = self.map[key]
        self.__skip(node)
        self.map.pop(key)

    def move_to_end(self, key):
        v, mru = self.map[key]
        self.__skip(mru)
        self.__push(mru)

    def __contains__(self, key):
        return key in self.map

    def __getitem__(self, key):
        v, _ = self.map[key]
        return v

    def __setitem__(self, key, value):
        node = Node(key)
        self.__push(node)
        self.map[key] = value, node

    def print(self):
        print(".....")
        node = self.dummy_head
        l = []
        while node:
            l.append(node.val)
            node = node.next
        print(f'list = {l}')
        print(f'map = {self.map.keys()}')
        print(".....\n")
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
