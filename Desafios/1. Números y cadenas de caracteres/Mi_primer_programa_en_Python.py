# Consigna

# Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:

# nota_1 cuenta como el 20% de la nota final
# nota_2 cuenta como el 30% de la nota final
# nota_3 cuenta como el 50% de la nota final

grade1=int(input("Ingrese primera nota:"))
grade2=int(input("Ingrese segunda nota:"))
grade3=int(input("Ingrese tercera nota:"))

finalGrade=grade1*0.2+grade2*0.3+grade3*0.5

print(f"Nota final: {finalGrade}")