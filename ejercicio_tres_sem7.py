# *Ejercicio Tres*
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

#los numeros impares terminan en alguno de estos numeros: 1,3,5,7,9
usuario=int(input('ingresa un número entero positivo: '))
for n in range(1, usuario+1, 2):
    print(n, end=", ")