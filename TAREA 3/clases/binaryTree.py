from clases.nodo import Nodo
from collections import deque

class BinaryTree:
    def __init__(self, root_data):
        if root_data is None :
            self.root = None
            self.size = 0
        else :
            self.root = Nodo(root_data)
            self.size = 1

    def isEmpty(self):
        return self.size == 0

    def isRoot(self, nodo):
        return nodo == self.root

    def isInternal(self, nodo):
        return nodo.get_left() is not None or nodo.get_right() is not None

    def hasLeft(self, nodo):
        return nodo.get_left() is not None

    def hasRight(self, nodo):
        return nodo.get_right() is not None

    def get_root(self):
        return self.root

    def get_left(self, nodo):
        return nodo.get_left()

    def get_right(self, nodo):
        return nodo.get_right()
    
    def parent(self, v):
        if self.isRoot(v):
            return None
        else:
            Q = deque()
            Q.append(self.get_root())
            temp = self.get_root()

            while Q and (self.get_left(Q[0]) != v and self.get_right(Q[0]) != v):
                temp = Q.popleft()

                if self.hasLeft(temp):
                    Q.append(self.get_left(temp))
                if self.hasRight(temp):
                    Q.append(self.get_right(temp))
            return temp if Q else None
        
    def depth(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.depth(self.parent(node))
        
    def height(self, node):
        if not self.isInternal(node):
            return 0
        else:
            h = 0
            h = max(self.height(self.get_left(node)), self.height(self.get_right(node)))
            return 1 + h
        
    def addRoot(self, w):
        self.root = Nodo(w)
        self.size = 1

    def insert_left(self, nodo, w):
        if nodo is not None:
            nodo_left = Nodo(w)
            nodo.set_left(nodo_left)
            self.size += 1

    def insert_right(self, nodo, w):
        if nodo is not None:
            nodo_right = Nodo(w)
            nodo.set_right(nodo_right)
            self.size += 1

    def remove(self, v):
        p = self.parent(v)
        if self.hasLeft(v) or self.hasRight(v):  # Caso 1: v tiene al menos un hijo
            if self.hasLeft(v):
                child = self.get_left(v)
            else:
                child = self.get_right(v)

            if self.get_left(p) == v:
                p.set_left(child)
            else:
                p.set_right(child)

            v.set_left(None)
            v.set_right(None)
        else:  # Caso 2: v no tiene hijos
            if self.get_left(p) == v:
                p.set_left(None)
            else:
                p.set_right(None)
        self.size -= 1

    def inorder(self, v):
        if self.hasLeft(v):
            self.inorder(self.get_left(v))
        print(v.get_data())  # Visitar el nodo
        if self.hasRight(v):
            self.inorder(self.get_right(v))
            