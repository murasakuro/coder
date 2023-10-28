# Crea un programa que pida por teclado (input) los datos de tus tres hobbies favoritos y los mismos se guarden en un archivo que 
# se llame miHobbieFavorito.txt.

with open("Desafios\8. Manejo de archivos y datos\miHobbieFavorito.txt","w") as archivo:
    faveHobbies=input("Ingrese sus Hobbies favoritos, separados por una coma:")
    faveHobbies=faveHobbies.split(",")
    for h in range(len(faveHobbies)):
        faveHobbies[h]=faveHobbies[h].strip()
        faveHobbies[h]=faveHobbies[h].capitalize()
        archivo.write(faveHobbies[h])
        archivo.write(".\n")