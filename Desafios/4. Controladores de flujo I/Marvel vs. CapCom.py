# Un curso se ha dividido en dos grupos diferentes: A y B de acuerdo al nombre y a una preferencia 
# (Marvel o Capcom). El grupo A está formado por fans de Marvel con un nombre anterior a la M y los 
# fans de Capcom con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que 
# pregunte al usuario su nombre y preferencia, y muestre por pantalla el grupo que le corresponde.

name=input("Ingrese su nombre: ")
preference=input( "Ingrese su preferencia (M o C): ")

if (preference=="M" and name<"M") or (preference=="C" and name>"N"):
    print("Usted pertenece al grupo A")
else: print("Usted pertenece al grupo B")