from collections import deque
class Nodo:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_left(self):
        return self._left

    def set_left(self, new_left):
        self._left = new_left

    def get_right(self):
        return self._right

    def set_right(self, new_right):
        self._right = new_right

class BinaryTree:
    def __init__(self, root_data):
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
    def depth(self,node):
        if node is None:
            return 0
        else:
            return 1+ self.depth(self.parent(node))
    def height(self,node):
        if not self.isInternal(node):
            return 0
        else:
            h=0
            h=max(self.get_left(node),self.height(self.get_right(node)))
            return 1+h
    def addRoot(self,w):
        self.root=Nodo(w)
        self.size=1
    def insert_left(self,nodo,w):
        if nodo is not None:
            nodo_left= Nodo(w)
            nodo.set_left(nodo_left)
            self.size+=1
    def insert_right(self,nodo,w):
        if nodo is not None:
            nodo_right= Nodo(w)
            nodo.set_right(nodo_right)
            self.size+=1
    from collections import deque
class Nodo:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_left(self):
        return self._left

    def set_left(self, new_left):
        self._left = new_left

    def get_right(self):
        return self._right

    def set_right(self, new_right):
        self._right = new_right

class BinaryTree:
    def __init__(self, root_data):
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
    def depth(self,node):
        if node is None:
            return 0
        else:
            return 1+ self.depth(self.parent(node))
    def height(self, node):
        if not self.isInternal(node):
            return 0
        else:
            h = 0
            h = max(self.height(self.get_left(node)), self.height(self.get_right(node)))
            return 1 + h
    def addRoot(self,w):
        self.root=Nodo(w)
        self.size=1
    def insert_left(self,nodo,w):
        if nodo is not None:
            nodo_left= Nodo(w)
            nodo.set_left(nodo_left)
            self.size+=1
    def insert_right(self,nodo,w):
        if nodo is not None:
            nodo_right= Nodo(w)
            nodo.set_right(nodo_right)
            self.size+=1
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
class BSTEntry:
    def __init__(self, e, key):
        self.data = e
        self.key = key
    def getData(self):
        return self.data
    def getKey(self):
        return self.key
    def setData(self, d):
        self.data = d
    def setKey(self, key):
        self.key = key
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
            temp = v

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
# Crear un objeto BinarySearchTree
abb = BinarySearchTree()

# Insertar datos en el ABB
abb.insert("Juan", 7)
abb.insert("Pablo", 4)
abb.insert("Maria", 9)
abb.insert("Ana", 2)
abb.insert("Diana", 10)
abb.insert("Mateo", 8)

# Imprimir el recorrido inorder para verificar la construcción del ABB
abb.inorder(abb.get_root())