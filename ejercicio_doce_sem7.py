# *Ejercicio Doce*
# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
# > Ejemplo
#NÚMEROS NEGATIVOS

#¿Cuántos valores va a introducir? -1 ¡ Imposible!

#NÚMEROS NEGATIVOS
#¿Cuántos valores va a introducir? 0
#No ha escrito ningún número negativo.

#NÚMEROS NEGATIVOS
#¿Cuántos valores va a introducir? 2
#Escriba el número 1:56
#Escriba el número 2: -22
#Ha escrito 1 número negativo.

#NÚMEROS NEGATIVOS
#¿Cuántos valores va a introducir? 5
#Escriba el número 1:56
#Escriba el número 2: -22
#Escriba el número 3: 98
#Escriba el número 4: -30
#Escriba el número 5:-30
#Ha escrito 3 números negativos.

print("NUMEROS NEGATIVOS ")
cantidad_numeros:int=int(input("¿Cuántos números vas a introducir? "))
negativos = 0
for i in range(cantidad_numeros):
    numero:int=float(input(f"Introduce el número {i+1}: "))
    if numero < 0:
        negativos += 1
print("Has introducido", negativos, "números negativos")