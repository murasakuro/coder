#  Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:

# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
lista0=list(range(0,11))
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
lista1=list(range(-10,1))
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
lista2=list(range(0,21,2))
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
lista3=list(range(-19,0,2))
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
lista4=list(range(0,51,5))

print(lista0)
print(lista1)
print(lista2)
print(lista3)
print(lista4)