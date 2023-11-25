import numpy as np

class Grafo :
    def __init__(self, V:list) -> None:
        self.V = sorted(V)
        self.matrix = np.zeros((len(self.V), len(self.V)), dtype=tuple)

    def agregarArista(self, A, B, KM, MINUTOS) :
        AIndex = self.V.index(A)
        BIndex = self.V.index(B)
        self.matrix[AIndex, BIndex] = (KM, MINUTOS)
        self.matrix[BIndex, AIndex] = (KM, MINUTOS)
