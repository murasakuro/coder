# Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y 
# realiza una media aritmética.

quantity=int(input("Ingrese la cantida de numeros que quiere promediar: "))
quantity2=quantity
sumation=0

while quantity2>0:
    sumation+=int(input("Ingrese un numero: "))
    quantity2-=1
average=(sumation/3)

print("El promedio es:", average)
    