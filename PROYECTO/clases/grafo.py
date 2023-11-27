import numpy as np

class Grafo :
    def __init__(self, V:list) -> None:
        self.V = sorted(V)
        self.matrixKm = np.zeros((len(self.V), len(self.V)), dtype=int)
        self.matrixMinutos = np.zeros((len(self.V), len(self.V)), dtype=int)

    def agregarArista(self, A, B, KM, MINUTOS) :
        AIndex = self.V.index(A)
        BIndex = self.V.index(B)

        # Agregar en matrixKm
        self.matrixKm[AIndex, BIndex] = KM
        self.matrixKm[BIndex, AIndex] = KM

        # Agregar en matrixMinutos
        self.matrixMinutos[AIndex, BIndex] = MINUTOS
        self.matrixMinutos[BIndex, AIndex] = MINUTOS

    def checkCarretera(self, A, B) :
        AIndex = self.V.index(A)
        BIndex = self.V.index(B)
        return not self.matrixKm[AIndex, BIndex] == 0
    
    def dijkstra(self, inicio, destino, modo='distancia') :
        # Verificar si los vértices dados existen en el grafo
        if inicio not in self.V or destino not in self.V :
            raise ValueError("Los vértices de inicio o destino no existen en el grafo.")

        # Seleccionar la matriz de pesos según el modo
        if modo == 'distancia' :
            matrix_peso = self.matrixKm
        elif modo == 'tiempo' :
            matrix_peso = self.matrixMinutos
        else:
            raise ValueError("Modo no válido. Debe ser 'distancia' o 'tiempo'.")

        # Inicializar acumulador de pesos, conjunto de vértices visitados y un diccionario para almacenar los padres
        pesos = {v: float('inf') for v in self.V}
        pesos[inicio] = 0
        visitados = set()
        padres = {v: None for v in self.V}

        while len(visitados) < len(self.V) :
            # Seleccionar el vértice no visitado con la distancia mínima
            actual = min(set(pesos.keys()) - visitados, key=lambda v: pesos[v])

            # Marcar el vértice como visitado
            visitados.add(actual)

            # Actualizar las pesos y los padres a los vértices adyacentes
            for vecino in self.V:
                if (self.checkCarretera(actual, vecino) and vecino not in visitados) :
                    peso = matrix_peso[self.V.index(actual), self.V.index(vecino)]
                    distancia_total = pesos[actual] + peso
                    if distancia_total < pesos[vecino] :
                        pesos[vecino] = distancia_total
                        padres[vecino] = actual

        # Reconstruir el camino desde el destino hasta el inicio
        camino = [destino]
        while padres[destino] is not None :
            destino = padres[destino]
            camino.insert(0, destino)

        # Tiempo o distancia total del viaje
        total = pesos[camino[-1]]

        return camino, total
