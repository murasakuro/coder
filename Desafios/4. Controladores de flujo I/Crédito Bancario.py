# Para aprobar un crédito, el cliente debe ser mayor de edad. Además, debe tener una antigüedad en 
# el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.  En caso no tenga la 
# antigüedad suficiente, su ingreso mensual debe ser como mínimo 4000 dólares. Si no cumple ninguna 
# de las condiciones, no se aprueba el crédito

age=int(input("Edad: "))
accountAge=int(input("Antiguedad de la cuenta en años: "))
income=int(input("Ingreso mensual en dolares: "))
if age>=18 and (accountAge>=3 and income>2500) or income>=4000:
    print("Su credito ha sido aprobado")
else: print("Su credito no ha sido aprobado")

    