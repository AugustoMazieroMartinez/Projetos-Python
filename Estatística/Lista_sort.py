from Node import Node
from typing import Optional
class Lista_Sort:
    head: Node
    tail: Node
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.tail == None
    def append(self, dado):
        newNode = Node(dado)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            
    def prepend(self, dado):
        newNode = Node(dado)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def lenght(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
            
    def remove(self, dado):
        if self.isEmpty():
            print('Nada Para Remover Bruh')
            return True
        
        current = self.head
        while current is not None:
            if current.value == dado:
                if current.prev == None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next != None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
            
        return False
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            if(current.next != None):
                print(' <-> ')
            current = current.next
            
    def bubble_sort(self):
        if self.isEmpty():
            return None
        
        end = None
        while end != self.head:
            swapped = False
            current = self.head
            
            while current.next != end:
                next = current.next
                if current.value > next.value:
                    current.value, next.value = next.value, current.value
                    swapped = True
                    
            if not swapped:
                break
            
            end = current