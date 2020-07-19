class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = None
        self.prev = None

class LFUCache:
    def __init__(self, capacity: int):
        self.freqs = []
        self.d = {}
        self.cap = capacity
        self.minfreq = None
        
    def create_DLL(self, node):
        head = Node(None, None, None)
        tail = Node(None, None, None)
        head.next = tail
        tail.prev = head
        self.addAtHead(node, head)
        return (head, tail)
        
    def addAtHead(self, node, head):
        node.next = head.next
        head.next.prev = node
        head.next = node
        head.next.prev = head
    
    def remove(self, node):
        node_next = node.next
        node_prev = node.prev
        node_next.prev = node_prev
        node_prev.next = node_next

    def update(self, node):
        freq = node.freq
        if len(self.freqs) == freq+1:
            self.remove(node)
            self.freqs.append(self.create_DLL(node))
        else:
            self.remove(node)
            self.addAtHead(node, self.freqs[freq+1][0])
        if self.minfreq == freq and not self.freqs[freq][0].next.val:
            self.minfreq += 1
        node.freq += 1
        
    def get(self, key: int) -> int:
        if self.cap == 0 or key not in self.d:
            return -1
        node = self.d[key]
        self.update(node)
        return node.val
            
    def put(self, key: int, value: int) -> None:
        if self.cap:
            if key in self.d:
                node = self.d[key]
                node.val = value
                self.update(node)
            else:
                if len(self.d) == self.cap:
                    del self.d[self.freqs[self.minfreq][1].prev.key]
                    self.remove(self.freqs[self.minfreq][1].prev)
                node = Node(key, value, 0)
                self.d[key] = node
                if not self.freqs:
                    self.freqs.append(self.create_DLL(node))
                else:
                    self.addAtHead(node, self.freqs[0][0])
                self.minfreq = 0
        