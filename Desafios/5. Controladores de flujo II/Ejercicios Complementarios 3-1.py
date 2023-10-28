# Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
options=("\n 1\) Sumar\n 2\) Restar\n 3\) Multiplicar\n 4\) Cancelar \n")

choice=int(input(f"Elija una opcion: {options}"))
# Mostrar una suma de los dos números
if choice==1: print(num1+num2)
# Mostrar una resta de los dos números (el primero menos el segundo)
elif  choice==2: print(num1-num2)
# Mostrar una multiplicación de los dos números
elif choice==3: print(num1*num2)
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
elif  choice==4: print("Finalizado")
# En caso de no introducir una opción válida, el programa informará de que no es correcta.
else: print("Opcion invalida")