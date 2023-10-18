from clases.listaSimple import ListaSimple

class Stack:
    def __init__(self) -> None:
        self.data = ListaSimple()

    def getSize(self):
        return self.data.getSize()
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def push(self, e):
        self.data.addFirst(e)

    def pop(self):
        return self.data.removeFirst()
    
    def top(self):
        if not self.isEmpty():
            return self.data.first().getData()
        else:
            return None
        
    def print(self) :
        self.data.print()
    