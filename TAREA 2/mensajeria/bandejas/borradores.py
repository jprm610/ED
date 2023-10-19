from clases.stack import Stack
from mensajeria.mensaje import Mensaje

class Borradores(Stack) :
    def __init__(self) -> None:
        super().__init__()

    def agregar(self, m:Mensaje) :
        self.push(m)

    def print(self) :
        if self.size == 0 : 
            print("No hay mensajes")
            return
        c = 1
        tmp = self.head
        while True :
            print(c, tmp.getData().toString())
            if tmp.getNext() == None : break
            tmp = tmp.getNext()
            c += 1
