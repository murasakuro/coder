tupla=(8,15,4,39,5,89,87,19,7,-755,88,123,2,11,15,9,355)

#imprimir en forma ordenada:
# el ultimo item
# el numero de items
# la posicion del item 87
# una lista con los ultimos tres items
# el item en la posicion 8 de la tupla
# el numero de veces que aparece el 7 en la tupla
lista=list(tupla[-3:])
print(tupla[-1],len(tupla),tupla.index(87),lista,tupla[8],tupla.count(7))