import pandas as pd
from clases.grafo import Grafo

def main() :
    carreteras = readData()

    G = construirGrafo(carreteras[:10])
    print(G.matrix)


def readData(path='Datos vias Colombia.csv') :
    data = pd.read_csv(path)
    data.columns = ['A', 'B', 'KM', 'MINUTOS']

    return data

def construirGrafo(df:pd.DataFrame) :
    # Vertices
    V = set(df['A'].to_list() + df['B'].to_list())

    G = Grafo(V)

    # Aristas
    for i in range(len(df)) :
        G.agregarArista(*df.loc[i].to_list())

    # Crear grafo
    return G

main()
