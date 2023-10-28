# Crear un conjunto en Python que posea los siguientes elementos:
# Países: Inglaterra, USA, México.
paises={"Inglaterra", "USA", "México"}
print(paises)

# Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA
paises.update(["Islandia", "Italia", "Argentina", "Portugal", "USA"])
print(paises)

# Elimina a los países: 
discard={"Chile", "Italia"}
paises-=discard
# paises.discard("Chile")
# paises.discard("Italia")
print(paises)