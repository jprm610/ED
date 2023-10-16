from clases.nodoDoble import NodoDoble

class listaDoble:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.size=0
    def getsize(self):
        return self.size
    def isEmpty(self):
        size=0
        return size
    def first():
        return self.head
    def last():
        return self.tail
    def addFirst(self, e: object):
        nodo = NodoDoble(e)
        if self.isEmpty:
            self.head = nodo
            self.tail = nodo
        else:
            nodo.setNext(self.head)
            self.head.setPrev(nodo)
            self.head = nodo
        self.size += 1

    def addLast(self,e:object):
        nodo=NodoDoble(e)
        if self.isEmpty():
            self.head=nodo
            self.tail=nodo
        else:
            self.tail.setNext(nodo)
            nodo.setPrev(self.tail)
            self.tail=nodo
            self.size+=1
    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            temp=self.head
            self.head= temp.getNext()
            temp.setNext(None)
            self.head.setPrev(None)
            self.size-=1
            return temp.getData()
    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            temp=self.tail
            self.tail=temp.getPrev()
            self.tail.setNext(None)
            temp.setPrev(None)
            self.size-=1
            return temp
    def remove(self, n):
        if n == self.head:
            return self.removeFirst()
        elif n == self.tail:
            return self.removeLast()
        else:
            e = n.data
            temp_prev = n.prev
            temp_next = n.next
            temp_prev.next = temp_next
            temp_next.prev = temp_prev
            n.next = None
            n.prev = None
            self.size -= 1
            return e
    def addBefore(self, n, e):
        if n == self.head:
            self.addFirst(e)
        else:
            m = NodoDoble(e)
            temp_prev = n.getPrev()
            temp_prev.setNext(m)
            m.setPrev(temp_prev)
            m.setNext(n)
            n.setPrev(m)
            self.size += 1

    def print(self):
        actual = self.head
        while actual:
            print(actual.data)  # Accede al atributo 'data' para imprimir el dato
            actual = actual.next


            








