from clases.queue import Queue
class Leido(Queue):
    def __init__(self) -> None:
        super().__init__()

    def add_mensaje(self,mensaje):
        self.enqueue(mensaje)

    def first_leidos(self):
       return self.first()
    
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
