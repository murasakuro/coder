# Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto
# se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

numbers=list(range(0,10))

numOfChoice=int(input("Ingrese un numero entero del 0 al 9:"))

while numOfChoice not in numbers:
    numOfChoice=int(input("Incorrecto, ingrese otro numero: "))
    
print("Correcto")