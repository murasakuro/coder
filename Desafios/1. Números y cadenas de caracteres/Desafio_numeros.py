# Descripción de la actividad.

# En nuestro trabajo, nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo.
# Para ello, debemos considerar tres aspectos:

# jugaron 20 partidos durante el torneo,
# los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos,
# el promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos

# La cantidad de partidos que debemos considerar a un equipo para el ejemplo se detallan a continuación:

# partidos_ganados 8
# partido_empatados 7
# partido_perdidos 5

# Importante: Cada una de las cantidades de partidos ganados, empatados o perdidos debe solicitarse al usuario utilizando la función input().
winPoints=3
drawPoints=1
lossPoints=0

wins=int(input("Victorias:"))
losses=int(input("Derrotas:"))
draws=int(input("Empates:"))
matches=wins+losses+draws

average=((wins*winPoints+draws)/matches)
print("El promedio de puntos por partido fué ",average)
print("El promedio de puntos por partido fué {average}")