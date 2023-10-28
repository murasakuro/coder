class Client:
    def __init__(self,name,surname,email,address):
        self.name=name
        self.surname=surname
        self.email=email
        self.address=address
    def __str__(self):
        return "Nombre: "+self.name+", Apellido: "+self.surname+", Email: "+self.email+", Direccion: "+self.address
    #metodo para ver los datos de un cliente
    def view_client_data(self):
        print(f'''
              Nombre completo: {self.name} {self.surname}
              Email: {self.email}
              Direccion: {self.address}
              ''')
    #metodo para cambiar los datos de un cliente
    def update_data(self,choice,new_value):
        if choice == 1:
            self.name = new_value
        elif choice == 2:
            self.surname = new_value
        elif choice == 3:
            self.email = new_value
        elif choice == 4:
            self.address = new_value