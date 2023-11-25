import pandas as pd
from clases.grafo import Grafo

def main() :
    carreteras = readData()

    G = construirGrafo(carreteras)


def readData(path='Datos vias Colombia.csv') :
    data = pd.read_csv(path)
    data.columns = ['A', 'B', 'KM', 'MINUTOS']

    return data

def construirGrafo(df:pd.DataFrame) :
    # Vertices
    V = set(df['A'].to_list() + df['B'].to_list())

    # Aristas
    E = []
    for i in range(len(df)) :
        E.append(tuple(df.loc[i]))

    # Crear grafo
    return Grafo(V, E)
