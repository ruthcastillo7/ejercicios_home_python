# *Ejercicio Seis*
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de la imagen adjunta.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

usuario:str=int(input("ingrese un numero entero: "))

for n in range(1, usuario + 1):
    for j in range(n * 2 - 1, 0, -2):
        print(j, end=" ")
    print()