#Programa 2: Ordenación de Arreglo Multidimensional

# Definir una función para ordenar la matriz en orden ascendente
def ordenar_matriz(matriz):
    # Aplanar la matriz
    matriz_aplanada = [valor for fila in matriz for valor in fila]
    # Ordenar la matriz aplanada
    matriz_aplanada.sort()
    # Volver a darle forma a la matriz ordenada
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz_aplanada.pop(0)

# Definir una matriz de ejemplo (3x3)
matriz = [
    [9, 4, 6],
    [2, 7, 1],
    [5, 3, 8]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

ordenar_matriz(matriz)  # Llama a la función para ordenar la matriz

print("\nMatriz ordenada en orden ascendente:")
for fila in matriz:
    print(fila)
