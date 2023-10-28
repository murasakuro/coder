# Crear un conjunto en Python que posea los siguientes elementos: 

# Colores: Rojo, Blanco, Azul.
colors={"Rojo", "Blanco", "Azul"}
print(colors)
# Posteriormente, agrega a nuestro set de colores, los valores de: Violeta y Dorado
colors.update(["Violeta", "Dorado"])
print(colors)
# Elimina a los colores: Celeste, Blanco y Dorado
colors.discard("Celeste")
colors.discard("Blanco")
colors.discard("Dorado")
print(colors)