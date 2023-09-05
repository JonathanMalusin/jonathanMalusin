#Programa 1: Búsqueda en Arreglo Multidimensional

# Definir una función para buscar un valor en una matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorremos las filas de la matriz
        for j in range(len(matriz[i])):  # Recorremos las columnas de cada fila
            if matriz[i][j] == valor:  # Comparamos el valor en la posición actual
                return f"El valor {valor} se encontró en la posición ({i}, {j})."  # Se encontró el valor
    return f"El valor {valor} no se encontró en la matriz."  # Valor no encontrado

# Definir una matriz de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_a_buscar = 8
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)