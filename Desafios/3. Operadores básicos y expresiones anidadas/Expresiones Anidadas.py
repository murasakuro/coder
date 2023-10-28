# A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se 
# cumplen todas las siguientes condiciones, encadenando operadores lógicos en una sola línea:

# NOMBRE sea diferente de cuatro asteriscos “****”
# EDAD sea mayor que 5 y a su vez menor que 20
# Que la longitud de NOMBRE sea mayor o igual a 4  pero a la vez menor que 8
# EDAD multiplicada por 3 sea mayor que 35


# Desde un input conseguir las variables:
# nombre = INPUT!!!
# edad = INPUT!!!!
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))

resultado=nombre!="****" and 5<edad<20 and 4<=len(nombre)<8 and (edad*3)>35
print("Las condiciones dan como resultado: ", resultado)