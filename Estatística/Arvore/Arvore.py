from Node import Node
class Arvore:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insertRec(self, root:Node, dado):
        if root == None:
            root = Node(dado)
            return self.root
        if dado < root.value:
            root.left = self.insertRec(root.left, dado)
        elif dado > root.value:
            root.right = self.insertRec(root.right, dado)
        return root
    def insert(self, dado):
        self.root = self.insertRec(self.root, dado)
    
    def searchRec(self, root:Node, dado):
        if root is None:
            return False
        if dado == root.value:
            return True
        if dado < root.value:
            return self.searchRec(root.left, dado)
        if dado > root.value:
            return self.searchRec(root.right, dado)
        return False
    
    def search(self, dado):
        return self.searchRec(self.root, dado)
    