# #clase cliente
# class Client:
#     def __init__(self,name,surname,email,address):
#         self.name=name
#         self.surname=surname
#         self.email=email
#         self.address=address
#     def view_client_data(self):
#         return(f'''
#               Nombre completo: {self.name} {self.surname}
#               Email: {self.email}
#               Direccion: {self.address}
#               ''')
#     def update_data(self,choice):
#         self.choice=input("Ingrese el nuevo dato: ")
#         return

# #menu
# def client_data_menu():
#     choice0=int(input("""
#     ======================================
#                      Menu
#     ======================================
#     Ingrese el numero de la opcion elegida
#     1. Crear cuenta
#     2. Actualizar datos de un usuario
#     3. Mostrar usuarios registrados
#     4. Salir
#     """))
#     if choice0==1:
#         input("Ingrese su nombre: ")
#         input("Ingrese su apellido: ")
#         input("Ingrese su email: ")
#         input("Ingrese su dirección: ")
#     elif choice0==2: 
#         alias=input("Ingrese el alias del cliente: ")
#         alias=alias.lower()
#         alias=alias.strip()
#         choice1=int(input("Que dato desea cambiar?\n1.Nombre\n2.Apellido\n3.Email\n4.Direccion\nIngrese cualquier numero para volver al menu principal\n"))
#         if choice1==1:alias.name=input("Ingrese el nuevo nombre: ")
#         elif choice1==2:alias.surname=input("Ingrese el nuevo apellido: ")
#         elif choice1==3:alias.email=input("Ingrese el nuevo email: ")
#         elif choice1==4:alias.address=input("Ingrese la nueva direccion: ")
#         else: exit()
#     elif choice0==3: 
#         pass
#     elif choice0==4:
#         exit()
#     else:
#         print("Opcion inválida, intente nuevamente")
#         client_data_menu()
 
# client_data_menu()


# #menu
# def client_data_menu():
#     choice0=int(input("""
#     ======================================
#                      Menu
#     ======================================
#     Ingrese el numero de la opcion elegida
#     1. Crear cuenta
#     2. Actualizar datos de un usuario
#     3. Mostrar usuarios registrados
#     4. Salir
#     """))
#     if choice0==1:
#         input("Ingrese su nombre: ")
#         input("Ingrese su apellido: ")
#         input("Ingrese su email: ")
#         input("Ingrese su dirección: ")
#     elif choice0==2: 
#         alias=input("Ingrese el alias del cliente: ")
#         alias=alias.lower()
#         alias=alias.strip()
#         choice1=int(input("Que dato desea cambiar?\n1.Nombre\n2.Apellido\n3.Email\n4.Direccion\nIngrese cualquier numero para volver al menu principal\n"))
#         if choice1==1:alias.name=input("Ingrese el nuevo nombre: ")
#         elif choice1==2:alias.surname=input("Ingrese el nuevo apellido: ")
#         elif choice1==3:alias.email=input("Ingrese el nuevo email: ")
#         elif choice1==4:alias.address=input("Ingrese la nueva direccion: ")
#         else: exit()
 
#     elif choice0==3: 
#         pass
#     elif choice0==4:
#         exit()
#     else:
#         print("Opcion inválida, intente nuevamente")
#         client_data_menu()

# def update_client_data(client):
#     choice1=int(input("Que dato desea cambiar?\n1.Nombre\n2.Apellido\n3.Email\n4.Direccion\nIngrese cualquier numero para volver al menu principal\n"))