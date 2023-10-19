from clases.listaSimple import ListaSimple

class Stack(ListaSimple):
    def __init__(self) -> None:
        super().__init__()
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def push(self, e):
        self.addFirst(e)

    def pop(self):
        return self.removeFirst()
    
    def top(self):
        if not self.isEmpty():
            return self.first().getData()
        else:
            return None
    