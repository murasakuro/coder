# Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente 
# utilizando la función input (). 
# Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit(). El programa 
# debe validar dicha acción. 
# Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida.

number=int(input("Ingrese un numero: "))
number2=number
operations=0

while number!=0:
    number=int(input("Ingrese otro numero para sumar, o 0 para terminar la operacion: "))
    number2+=number
    operations+=1
    print(f"El resultado de la suma es {number2} con {operations} operaciones.")
else: print(f"El resultado final de la suma es {number2} con {operations} operaciones.")