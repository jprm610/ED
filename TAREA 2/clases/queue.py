from clases.listaSimple import ListaSimple

class Queue :
    def __init__(self) -> None:
        self.data = ListaSimple()

    def getSize(self) :
        return self.data.getSize()
    
    def isEmpty(self) :
        return self.getSize() == 0
    
    def enqueue(self, e:object) :
        self.data.addLast(e)

    def dequeue(self) :
        if self.isEmpty() :
            return None
        else :
            return self.data.removeFirst()
        
    def first(self) :
        if self.isEmpty() :
            return None
        else :
            return self.data.first().getData()

    def print(self) :
        self.data.print()
