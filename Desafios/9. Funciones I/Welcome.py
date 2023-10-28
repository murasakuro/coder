# Escribir una función a la que se le pase una cadena del nombre de una ciudad <ciudad> y muestre por pantalla el saludo 
# ¡hola bienvenidx a <nombre>!.

def welcome(city):
    print(f"¡hola bienvenidx a {city}!.")

welcome(input("Ingrese el nombre de la ciudad: "))