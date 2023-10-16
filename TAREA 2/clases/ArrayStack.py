from clases.listaSimple import ListaSimple
class Stack:
    def __init__(self,lista) -> None:
        self.data= lista
    def getSize(self):
        return self.data.size
    def isEmpty(self):
         return self.data.size == 0
    def push(self,e):
        self.data.addFirst(e)
    def pop(self):
        return self.data.removeFirst()
    def top(self):
        if self.isEmpty():
            return self.data.first().getData()
        else:
            return None
    def print(self):
        current = self.data.head
        while current is not None:
            print(current.getData())
            current = current.getNext()
    