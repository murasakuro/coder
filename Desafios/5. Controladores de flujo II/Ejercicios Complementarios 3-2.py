# Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso
# hasta que lo introduzca correctamente.
number=int(input("Ingrese un numero: "))
while number%2==0:
     number=int(input("Invalido, ingrese otro numero: "))
else: print("Numero Impar")