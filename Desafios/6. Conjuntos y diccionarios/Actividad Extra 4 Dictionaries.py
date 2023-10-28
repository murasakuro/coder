# Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre 
# por pantalla:

name=input("Ingrese su nombre: ")
age=int(input("Ingrese su edad: "))
adress=input("Ingrese su direccion: ")

account={
    "Nombre":name,
    "Edad":age,
    "Direccion":adress
}

for item in account.items():
    print(item)