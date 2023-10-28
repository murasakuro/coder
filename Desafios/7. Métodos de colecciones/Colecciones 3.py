# Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}. 
currency={'Dolar':'$',
          'Euro':'€', 
          'Libra':'£'}
# Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar. 
chosenCurrency=input("Ingrese la divisa elegida: ") 
chosenCurrency=(chosenCurrency.strip()).capitalize()
if chosenCurrency not in currency.keys(): print("La divisa no se encuentra disponible.")
else: print(f"El simbolo de la divisa {currency.get(chosenCurrency)}")
# En el caso de ingresar una divisa no existente en nuestro diccionario, deberemos indicarle con un mensaje de notificación que la 
# divisa no se encuentra disponible. 
