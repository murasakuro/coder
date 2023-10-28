# Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado. 
# Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: “No existe 
# generación asociada”

birthYear=int(input("Su año de nacimiento: "))
if 1920<=birthYear<=1940: print("Usted es de la generacion Silenciosa")
elif 1946<=birthYear<=1964: print("Usted es de la generacion Baby Boomer")
elif 1965<=birthYear<=1979: print("Usted es de la generacion X")
elif 1980<=birthYear<=2000: print("Usted es de la generacion Y")
elif 2001<=birthYear<=2010: print("Usted es de la generacion Z")
else: print("No existe generacion asociada")