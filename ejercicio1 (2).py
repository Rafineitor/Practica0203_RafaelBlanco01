#Contraseña.

A = (input("Introduzca su contraseña: "))
B = (input("Introduzca de nuevo su contraseña: "))
cont_1 = A.lower()
cont_2 = B.lower()
if cont_1==cont_2:
    print ("Las contraseñas ingresadas coinciden.")
else:
    print ("las contraseñas ingresadas no coinciden.")