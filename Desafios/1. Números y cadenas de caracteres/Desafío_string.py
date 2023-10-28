# Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia. De forma individual, realiza lo siguiente:

# Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada. Para devolver una cadena dada vuelta se usa el tercer índice negativo con slicing: cadena[::-1].
# Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
# Extraer la nota y almacenarla en una variable llamada nota.
# Extraer la materia y almacenarla en una variable llamada materia.
# Mostrar por pantalla la siguiente estructura: 😎NOMBRE APELLIDO ha sacado un NOTA en MATERIA. Esto ultimo hacerlo, formateando las anteriores variables en una variable llamada cadena_formateada
# cadena = “acitametaM ,5.8 ,otipeP ordeP”
#1
chain="acimiuQ ,9 ,arrabI niuqaoJ"
invertedChain=chain[::-1]

print(invertedChain)

studentName=invertedChain[0:14]
studentGrade=invertedChain[16]
subject=invertedChain[19:26]

print(f"{studentName} se ha sacado un {studentGrade} en {subject}")
