#Verificacion contraseña.

contraseña = input("Ingrese su contraseña: ")
contraseña1 = input("Ingrese su contraseña nuevamente")

while contraseña != contraseña1:
    contraseña1 = input("Ingrese su contraseña nuevamente: ")
if contraseña == contraseña1:
    exit()