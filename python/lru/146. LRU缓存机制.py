class DNode:
    def __init__(self,key=0,value=0):
        self.pre = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        self.capacity = capacity
        self.size = 0

        self.head = DNode()
        self.tail = DNode()
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            node.value = value
        else:
            node = DNode(key,value)
            self.addToHead(node)
            self.cache[key] = node
            self.size += 1
            if self.capacity < self.size:
                node  = self.deleteTail()
                self.size -= 1
                self.cache.pop(node.key)

    def moveToHead(self,node):
        self.deleNode(node)
        self.addToHead(node)

    def deleNode(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def addToHead(self,node):
        node.next = self.head.next
        node.next.pre = node
        self.head.next = node
        node.pre = self.head

    def deleteTail(self):
        node = self.tail.pre
        self.deleNode(node)
        return node


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

