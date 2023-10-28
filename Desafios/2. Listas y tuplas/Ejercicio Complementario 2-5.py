# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el 
# cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar 
# las sumas incorrectas utilizando la técnica del slicing?
# Partirás de: 
# matriz = [ 
#     [1, 5, 1],
#     [2, 1, 2],
#     [3, 0, 1],
#     [1, 4, 4]
# ]
# Debes llegar a: 
# matriz = [ 
#     [1, 5, 1, 7],
#     [2, 1, 2, 5],
#     [3, 0, 1, 4],
#     [1, 4, 4, 9]
# ]

matriz=[ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
 ]

for item in matriz:
    item.append(sum(item))
print(matriz)
