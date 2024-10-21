from Node import Node
class Fila:
    def __init__(self):
        self.first = None
        self.last = None
    
    def isEmpty(self):
        return self.first == None
    
    def push(self, dado):
        newNode = Node(dado)
        if self.isEmpty():
            self.first = newNode
        else:
            self.last.next = newNode
        self.last = newNode
    
    def pop(self):
        if self.isEmpty():
            return print('Vazio')
        removedNode = self.first
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return removedNode.value

    def peek(self):
        if self.isEmpty():
            return print('Vazio')
        return self.first.value
    
    def inversor(self, fila):
        if(fila.isEmpty()):
            return ''
        else:
            retorno = fila.pop()
            return self.inversor(fila) + retorno
        
    def inverteString(self, dado):
        fila = Fila()
        for ch in dado:
            fila.push(ch)
        novaString = self.inversor(fila)
        return novaString