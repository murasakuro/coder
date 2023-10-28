from Paquete.Modulo1 import Client

client0=Client("Joaquin","Ibarra","juacoibarra02@gmail.com","direccion 1234")

print(client0)

client0.view_client_data()

client0.update_data(1,"nuevo nombre")
client0.update_data(2,"nuevo apellido")
client0.update_data(3,"nuevo mail")
client0.update_data(4,"nueva direccion")

client0.view_client_data()