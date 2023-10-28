# A partir de una lista realizar las siguientes tareas sin modificar la lista original:
lista=[29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]

# Borrar los elementos duplicados
listaFinal=list(set(lista))
print(listaFinal)
# Ordenar la lista de mayor a menor
listaFinal.sort(reverse=True)
print(listaFinal)
# Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
listaCopy=listaFinal.copy()
for num in listaFinal:
    if num%2==1:listaCopy.remove(num)
listaFinal=listaCopy
print(listaFinal)
# Realizar una suma de todos los números que quedan (sum(lista))
print(sum(listaFinal))
# Añadir como primer elemento de la lista la suma realizada insert(0, suma)
listaFinal.insert(0,sum(listaFinal))
print(listaFinal)
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el 
# primer número de la lista
print("El primer valor de la lista es igual a la suma del resto de valores?",listaFinal[0]==(sum(listaFinal[1:])))