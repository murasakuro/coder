#Diccionario que hace de base de datos
data_base={"Joaquin":"Joaquin123"}

#Funcion del menu
def menu():
    choice=int(input("""
    ================================
                  Menu
    ================================
    1. Crear cuenta
    2. Iniciar sesion
    3. Mostrar usuarios registrados
    4. Salir
    """))
    if choice==1:
        sign_up()
    elif choice==2: 
        login()
    elif choice==3: 
        read_data()
    elif choice==4:
        exit()
    else:
        print("Opcion inválida, intente nuevamente");menu()

#Funcion para crear cuenta
def sign_up():
    conditions_met=False
    user=input(r"Ingrese un nombre de usuario (usar letras exclusivamente): ")
    password=input(r"Ingrese una contraseña (usar letras y numeros exclusivamente): ")
    while not conditions_met:
        #Chequeo que ambos valores ingresado cumplan las condiciones
        if user.isalpha() and password.isalnum():
            #Chequeo que el nombre de usuario ingresado este libre en la base de datos
            if user not in data_base.keys():
               conditions_met=1
               data_base.setdefault(user,password)
               menu()
            else:
                print("Nombre de usuario ya existente, intente nuevamente.")
                user=input(r"Ingrese un nombre de usuario (usar letras exclusivamente): ")
                password=input(r"Ingrese una contraseña (usar letras y numeros exclusivamente): ")
        #Chequeo si el nombre ingresad0 no cumple las condiciones
        elif not user.isalpha():
            print("El nombre de usuario no cumple con las condiciones, intente nuevamente.")
            user=input(r"Ingrese un nombre de usuario (usar letras exclusivamente): ")
        #Chequeo si la contraseña ingresada no cumple las condiciones
        elif not password.isalnum():
            print("La contraseña no cumple con las condiciones, intente nuevamente.")
            password=input(r"Ingrese una contraseña (usar letras y numeros exclusivamente): ")
        #Chequeo si ambos valores ingresados no cumplen las condiciones
        if not user.isalpha() and not password.isalnum():
            print("El nombre de usuario y la contraseña no cumplen con las condiciones, intente nuevamente.")
            user=input(r"Ingrese un nombre de usuario (usar letras exclusivamente): ")
            password=input(r"Ingrese una contraseña (usar letras y numeros exclusivamente): ")
            
#Funcion para ver la base de datos
def read_data():
    print("Aca tiene una lista de cada usuario, con su contraseña:")
    for user, password in data_base.items():
        print(f"Usuario:{user}, Contraseña:{password}")

#Funcion para inicio de sesion     
def login():
    #Cantidad de contraseñas incorrectas permitidas
    counter=5
    user=input("Ingrese su nombre de perfil: ")
    #Chequeo que el nombre de usuario se encuentre en la base de datos, en caso de que no, vuelve a iniciar la funcion
    if user not in data_base.keys(): login()
    password=input("Ingrese su contraseña: ")
    #Chequeo que la contraseña ingresada coincida con el usuario
    if data_base[user]==password: print(f"Bienvenido {user}!")
    else:
        while counter>0:
            counter-=1
            input(f"Contraseña incorrecta, le quedan {counter} intentos.")
        if counter==0:print("No le quedan más intentos.");exit()

menu()