from clases.nodoDoble import NodoDoble

class ListaDoble:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getsize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def first(self):
        return self.head
    
    def last(self):
        return self.tail
    
    def get(self, i) :
        if i >= self.getsize() : raise Exception("i out of bounds!")
        c = 0
        tmp = self.head
        while True :
            if c == i : return tmp.getData()
            tmp = tmp.getNext()
            c += 1

    def addFirst(self, e:object):
        nodo = NodoDoble(e)
        if self.isEmpty() :
            self.head = nodo
            self.tail = nodo
        else:
            nodo.setNext(self.head)
            self.head.setPrev(nodo)
            self.head = nodo
        self.size += 1

    def addLast(self, e:object):
        nodo = NodoDoble(e)
        if self.isEmpty() :
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.setNext(nodo)
            nodo.setPrev(self.tail)
            self.tail = nodo
            self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        elif self.size == 1 :
            tmp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return tmp.getData()
        else:
            temp = self.head
            self.head = temp.getNext()
            temp.setNext(None)
            self.head.prev = None
            self.size -= 1
            return temp.getData()
        
    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            temp = self.tail
            self.tail = temp.getPrev()
            self.tail.setNext(None)
            temp.setPrev(None)
            self.size -= 1
            return temp
        
    def remove(self, n):
        # Find node

        node = None
        tmp = self.head
        while True :
            if tmp.getData() == n :
                node = tmp
                break
            if tmp.getNext() == None : break
            tmp = tmp.getNext()
        if node == None : return False

        # Remove the node
        if node == self.head:
            return self.removeFirst()
        elif node == self.tail:
            return self.removeLast()
        else:
            temp_prev = node.getPrev()
            temp_next = node.getNext()
            temp_prev.next = temp_next
            temp_next.prev = temp_prev
            node.next = None
            node.prev = None
            self.size -= 1
            return node.getData()
        
    def addBefore(self, n, e:object):
        # Find node
        node = None
        tmp = self.head
        while True :
            if tmp.getData() == n :
                node = tmp
                break
            if tmp.getNext() == None : break
            tmp = tmp.getNext()
        if node == None : return False

        if node == self.head:
            self.addFirst(e)
        else:
            m = NodoDoble(e)
            temp_prev = node.getPrev()
            temp_prev.setNext(m)
            m.setPrev(temp_prev)
            m.setNext(node)
            node.setPrev(m)
            self.size += 1

    def addAfter(self, n, e:object) :
        # Find node
        node = None
        tmp = self.head
        while True :
            if tmp.getData() == n :
                node = tmp
                break
            if tmp.getNext() == None : break
            tmp = tmp.getNext()
        if node == None : return False

        if node == self.tail :
            self.addLast(e)
        else :
            m = NodoDoble(e)
            temp_next = node.getNext()
            node.setNext(m)
            m.setPrev(node)
            m.setNext(temp_next)
            temp_next.setPrev(m)
            self.size += 1

    def print(self) :
        c = 1
        node = self.head
        while True :
            print(c, node.getData())
            if node.getNext() == None : break
            node = node.getNext()
            c += 1
        print(f"Size: {self.size}")


            








