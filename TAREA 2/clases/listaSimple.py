from clases.nodoSimple import NodoSimple

class ListaSimple :
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self) :
        return self.size
    
    def isEmpty(self) :
        return self.size == 0
    
    def setSize(self, size) :
        self.size = size

    def first(self) :
        return self.head
    
    def last(self) :
        return self.tail
    
    def addFirst(self, e:object) :
        node = NodoSimple(e)
        if self.isEmpty() :
            self.head = node
            self.tail = node
        else :
            node.setNext(self.head)
            self.head = node
        self.setSize(self.size + 1)

    def addLast(self, e:object) :
        node = NodoSimple(e)
        if self.isEmpty() :
            self.head = node
            self.tail = node
        else :
            self.tail.setNext(node)
            self.tail = node
        self.setSize(self.size + 1)

    def removeFirst(self) :
        if self.isEmpty() : return None
        temp = self.head
        self.head = temp.getNext()
        temp.setNext(None)
        self.setSize(self.size - 1)
        return temp.getData()
    
    def removeLast(self) :
        if self.isEmpty() : return None
        temp = self.tail
        anterior = self.head
        while anterior.getNext() != self.tail :
            anterior = anterior.getNext()
        anterior.setNext(None)
        self.tail = anterior
        self.setSize(self.size - 1)
        return temp.getData()
    
    def print(self) :
        c = 1
        node = self.head
        while True :
            print(c, node.getData())
            if node.getNext() == None : break
            node = node.getNext()
            c += 1
        