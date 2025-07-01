from Node import Node

class Lista:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head, self.tail = newNode, newNode
            return True
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            return True
        return False
    
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head, self.tail = newNode, newNode
            return True
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return True
        return False
    
    def remove(self, value):
        if self.head is None: 
            return False
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False
    
    def search(self, value):
        if self.head is None:
            return False
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    