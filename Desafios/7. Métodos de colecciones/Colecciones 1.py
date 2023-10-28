texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
#print(texto)

# Transformar a:
# Gordon lanzó su curva...
# - Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# - Dos pies le corrigió Troop.
# - Strawberry menea la cabeza como disgustado… -agrega el comentarista.

lineas = texto.split("&") 

# Para probra como quedo la lista cuando hicimos el split("&") --> Recordar que split devuelve una lista desde una cadena
#lineas[0]+=".."
for i, linea in enumerate(lineas):
    lineas[i]=linea[0].upper()+linea[1:]
    if i!=0:lineas[i] ="- "+lineas[i]

textoFinal=".\n".join(lineas)+(".")
print(textoFinal)

# Mostramos el texto final
#for linea in lineas:
#    print(linea)