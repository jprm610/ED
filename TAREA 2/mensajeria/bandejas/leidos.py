from clases.nodoSimple import Queue
class Leido:
    def __init__(self) -> None:
        self.bandeja_leidos=Queue()
    def add_mensaje(self,mensaje):
        self.bandeja_leidos.enqueue(mensaje)
    def first_leidos(self):
       return self.bandeja_leidos.first()
