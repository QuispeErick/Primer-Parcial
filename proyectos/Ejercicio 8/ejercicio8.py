import itertools

#  nodos
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


# matriz
matriz_adyacencia = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 0, 8, 9, 10, 11, 12, 13],
    [2, 8, 0, 14, 15, 16, 17, 18],
    [3, 9, 14, 0, 19, 20, 21, 22],
    [4, 10, 15, 19, 0, 23, 24, 25],
    [5, 11, 16, 20, 23, 0, 26, 27],
    [6, 12, 17, 21, 24, 26, 0, 28],
    [7, 13, 18, 22, 25, 27, 28, 0]
]


def calcular_costo_camino(camino, matriz, nodos):
    costo_total = 0
    detalles_camino = []
    for i in range(len(camino) - 1):
        nodo_actual = nodos.index(camino[i])
        siguiente_nodo = nodos.index(camino[i + 1])
        costo = matriz[nodo_actual][siguiente_nodo]
        costo_total += costo
        detalles_camino.append(f"{camino[i]}->{costo}->{camino[i + 1]}")
    return detalles_camino, costo_total


# Genera caminos posibles
for nodo_inicial in nodos:
    nodos_restantes = [nodo for nodo in nodos if nodo != nodo_inicial]
    permutaciones = itertools.permutations(nodos_restantes)

    for camino_parcial in permutaciones:
        camino_completo = [nodo_inicial] + list(camino_parcial)
        detalles_camino, costo_total = calcular_costo_camino(camino_completo, matriz_adyacencia, nodos)
        print('->'.join(detalles_camino))
        print(f"Total del camino: {costo_total}")
