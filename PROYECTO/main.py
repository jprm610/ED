import pandas as pd
from clases.grafo import Grafo

def main() :
    carreteras = readData()

    G = construirGrafo(carreteras)
    print('Grafo construido.')

    while True :
        print('FUNCIONALIDADES')
        print('1) Existencia de carretera entre A y B')
        print('2) Camino más corta entre A y B (Kilómetros)')
        print('3) Camino más corta entre A y B (Minutos)')
        entrada = int(input('Elija una funcionalidad o 0 para terminar: '))
        if entrada == 1 : func1(G)
        elif entrada == 2 : func2(G)
        elif entrada == 3 : func3(G)
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
    if A not in G.V or B not in G.V : raise ValueError('Verifique las ciudades ingresadas')

    hayCarretera = G.checkCarretera(A=A, B=B)
    if hayCarretera : print('Sí hay carretera')
    else : print('No hay carretera')

    return

def func2(G: Grafo) :
    print("2) Camino más corta entre A y B (Kilómetros)")
    A = input('Elija ciudad A: ')
    B = input('Elija ciudad B: ')
    if A not in G.V or B not in G.V : raise ValueError('Verifique las ciudades ingresadas')
    camino, distancia = G.dijkstra(inicio=A, destino=B, modo='distancia')
    print('El camino más corto por distancia es: ', end='')
    print(*camino, sep=' -> ', end='')
    print(f' con una distancia total de {distancia} kilómetros.')

def func3(G: Grafo) :
    print("3) Camino más corta entre A y B (Minutos)")
    A = input('Elija ciudad A: ')
    B = input('Elija ciudad B: ')
    if A not in G.V or B not in G.V : raise ValueError('Verifique las ciudades ingresadas')
    camino, tiempo = G.dijkstra(inicio=A, destino=B, modo='tiempo')
    print('El camino más corto por tiempo es: ', end='')
    print(*camino, sep=' -> ', end='')
    print(f' con un tiempo total de {tiempo} minutos.')

main()
