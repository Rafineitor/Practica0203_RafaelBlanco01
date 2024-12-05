#Triangulo de numeros.

numero = int(input("Ingrese un numero: "))

for n in range (1, numero+1):
    for i in range(n):
        print(2*(n-i)-1, end=" ")
    print()