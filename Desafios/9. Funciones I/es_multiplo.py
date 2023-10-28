# Crea un programa que le pida dos números enteros al usuario y diga por consola, si alguno de ellos es múltiplo del otro. La 
# función debe llamarse es_multiplo().

def es_multiplo(num1, num2):
    if num1==num2: print("Los numeros son iguales, por lo que son multiplos entre si.")
    elif num1==0 or num2==0: print(f"El 0 es multiplo del otro.")
    elif type(num1//num2)==int and type(num2/num1)==int: print("Los numeros son multiplos entre si.")
    elif type(num1//num2)==int: print(f"El {num2} es multiplo del {num1}.")
    elif type(num2//num1)==int: print(f"El {num1} es multiplo del {num2}.")
    else: print("Los numeros no son multiplos.")

es_multiplo(int(input("Ingrese un numero entero: ")),int(input("Ingrese otro numero entero: ")))