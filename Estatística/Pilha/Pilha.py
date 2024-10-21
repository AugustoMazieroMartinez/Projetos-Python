from Node import Node
class Pilha:
    def __init__(self):
        self.top = None
    def push(self, dado):
        newNode = Node(dado)
        newNode.next = self.top
        self.top = newNode
    def isEmpty(self):
        return self.top == None
    def pop(self):
        if self.isEmpty():
            return print('Vazio')
        removeNode = self.top.value
        self.top = self.top.next
        return removeNode
    def peek(self):
        if self.isEmpty():
            return print('Vazio')
        return self.top.value
    def inverteString(self, dado):
        stack = Pilha()
        novaString = ''
        for ch in dado:
            stack.push(ch)
        while not stack.isEmpty():
            novaString += stack.pop()
        return novaString
    