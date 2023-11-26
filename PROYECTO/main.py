import pandas as pd
from clases.grafo import Grafo

def main() :
    carreteras = readData()

    G = construirGrafo(carreteras)
    print('Grafo construido.')

    while True :
        print('FUNCIONALIDADES')
        print('1) Existencia de carretera entre A y B')
        print('2) Carretera más corta entre A y B (Kilómetros)')
        print('3) Carretera más corta entre A y B (Minutos)')
        entrada = int(input('Elija una funcionalidad o 0 para terminar: '))
        if entrada == 1 : func1(G)
        elif entrada == 2 : pass
        elif entrada == 3 : pass
        else : break
    print('Programa terminado.')
    return

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

def func1(G: Grafo) :
    print('1) Check carretera entre A y B')
    A = input('Elija ciudad A: ')
    B = input('Elija ciudad B: ')
    if A not in G.V or B not in G.V : raise Exception('Verifique las ciudades ingresadas')

    hayCarretera = G.checkCarretera(A, B)
    if hayCarretera : print('Sí hay carretera')
    else : print('No hay carretera')

    return

main()
