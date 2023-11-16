from clases.binaryTree import BinaryTree
from clases.BSTEntry import BSTEntry
from clases.nodo import Nodo

class BinarySearchTree(BinaryTree):
    def __init__(self, root_data=None):
        super().__init__(root_data)

    def find(self, k):
        return self.searchTree(k, self.get_root())

    def searchTree(self, key, v):
        if v is None:
            return None  # El árbol está vacío, no se puede encontrar nada
        u = v.get_data()

        if key == v.getKey():  # Caso base
            return v
        elif key < v.getKey():
            return self.searchTree(key, v.get_left())
        else:
            return self.searchTree(key, v.get_right())

    def insert(self, e, k):
        new_entry = BSTEntry(e, k)

        if self.isEmpty():
            self.addRoot(new_entry)
        else:
            self.addEntry(self.get_root(), new_entry)

    def addEntry(self, v, new_entry):
        if v is None:
            self.set_root(Nodo(new_entry))
            self.size += 1
        else:
            temp = v.get_data()

            if new_entry.getKey() < temp.getKey():
                if self.hasLeft(v):
                    self.addEntry(v.get_left(), new_entry)
                else:
                    v.set_left(Nodo(new_entry))
                    self.size += 1
            else:
                if self.hasRight(v):
                    self.addEntry(v.get_right(), new_entry)
                else:
                    v.set_right(Nodo(new_entry))
                    self.size += 1

    def predecessor(self, v):
        temp = v.get_left()
        return self.maxNode(temp)
    def maxNode(self, temp):
        if self.hasRight(temp):
            return self.maxNode(temp.get_right())
        else:
            return temp