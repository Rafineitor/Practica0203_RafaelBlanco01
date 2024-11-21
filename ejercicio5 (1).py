#Jarri Poter.

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (masculino o femenino): ")
letra = nombre[0].lower()

if letra < "m" and sexo == "femenino":
    print("Perteneces a Gryffindor")
elif letra > "n" and sexo == "masculino":
    print("Perteneces a Gryffindor")
else:
    print("Perteneces a Slytheryn")