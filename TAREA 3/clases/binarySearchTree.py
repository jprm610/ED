from clases.binaryTree import BinaryTree
from clases.BSTEntry import BSTEntry
from clases.nodo import Nodo
import graphviz

class BinarySearchTree(BinaryTree):
    def __init__(self, root_data=None):
        super().__init__(root_data)

    def find(self, k):
        return self.searchTree(k, self.get_root())

    def searchTree(self, key, v):
        if v is None:
            return None  # El árbol está vacío, no se puede encontrar nada

        if isinstance(v.get_data(), BSTEntry):
            u = v.get_data()
            if key == u.getKey():  # Caso base
                return v
            elif key < u.getKey():
                return self.searchTree(key, v.get_left())
            else:
                return self.searchTree(key, v.get_right())
        else:
            # Si v no es un nodo de tipo BSTEntry, asumimos que es un nodo sin datos asociados.
            # Puedes ajustar esta lógica según tu implementación específica.
            return None


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

   
    def maxNode(self):
        return self.maxNodeFrom(self.get_root())

    def maxNodeFrom(self, temp):
        if self.hasRight(temp):
            return self.maxNodeFrom(temp.get_right())
        else:
            return temp
    
    def minNode(self):
        return self.minNodeFrom(self.get_root())

    def minNodeFrom(self, temp):
        if self.hasLeft(temp):
            return self.minNodeFrom(temp.get_left())
        else:
            return temp

    def remove(self, k):
        v = self.find(k)
        if v:
            temp = v.get_data()

            if self.hasLeft(v) and self.hasRight(v):  # Caso 2: v tiene ambos hijos
                w = self.predecessor(v)
                v.set_data(w.get_data())
                super().remove(w)
            else:  # Caso 1: v tiene cero o un hijo
                super().remove(v)

            return temp

    def predecessor(self, v):
        temp = v.get_left()
        while self.hasRight(temp):
            temp = temp.get_right()
        return temp


    def __str__(self):
        return self.inorder_str(self.get_root())

    def inorder_str(self, v):
        if v is None:
            return ""
        result = self.inorder_str(self.get_left(v))
        result += f"({v.get_data().getKey()}, {v.get_data().getData()}) "
        result += self.inorder_str(self.get_right(v))
        return result
    
    def visualize_tree(self):
        dot = graphviz.Digraph()
        self._add_nodes_edges(dot, self.root)
        dot.render('binary_tree', view=True, format='png')

    def _add_nodes_edges(self, dot, entry):
        if entry:
            dot.node(str(entry.get_data().getKey()), label=str(entry.get_data().getData()))
            if self.hasLeft(entry):
                left_child = self.get_left(entry)
                dot.edge(str(entry.get_data().getKey()), str(left_child.get_data().getKey()))
                self._add_nodes_edges(dot, left_child)
            if self.hasRight(entry):
                right_child = self.get_right(entry)
                dot.edge(str(entry.get_data().getKey()), str(right_child.get_data().getKey()))
                self._add_nodes_edges(dot, right_child)

    
