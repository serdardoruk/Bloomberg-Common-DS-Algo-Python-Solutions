class DoublyLinkedList:
    def __init__(self):
        self.val = 0
        self.key = 0
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _removeNode(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
    
    def _moveToHead(self, node):
        self._removeNode(node)
        self._addNode(node)
        
    def _popTail(self):
        prevNode = self.tail.prev
        self._removeNode(prevNode)
        return prevNode
        
    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._moveToHead(node)
        return node.val

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            newNode = DoublyLinkedList()
            newNode.val = value
            newNode.key = key
            
            self.cache[key] = newNode
            self._addNode(newNode)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._popTail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self._moveToHead(node)
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)