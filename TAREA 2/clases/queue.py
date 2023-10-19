from clases.listaSimple import ListaSimple

class Queue(ListaSimple) :
    def __init__(self) -> None:
        super().__init__()
    
    def enqueue(self, e:object) :
        self.addLast(e)

    def dequeue(self) :
        if self.isEmpty() :
            return None
        else :
            return self.removeFirst()
        
    def first(self) :
        if self.isEmpty() :
            return None
        else :
            return super().first().getData()
