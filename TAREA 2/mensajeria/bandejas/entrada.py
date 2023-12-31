from clases.listaDoble import ListaDoble
from mensajeria.mensaje import Mensaje

class Entrada(ListaDoble) :
    def __init__(self) -> None:
        super().__init__()

    def agregar(self, m:Mensaje) :
        self.addFirst(m)

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

    def toList(self) -> list :
        lista = []
        if self.isEmpty() : return lista
        tmp = self.head
        while True :
            lista.append(tmp.getData())
            if tmp.getNext() == None : break
            tmp = tmp.getNext()
        return lista
