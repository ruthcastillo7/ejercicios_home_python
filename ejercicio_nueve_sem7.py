#*Ejercicio Nueve*
# Escriba un programa que pregunte cuántos números se van a introducir
numeros_a_introducir:str=float(input("¿Cuántos números se va a introducir?: "))
# luego pida esos números
numero_anterior:str=int(input("escriba sus numeros: "))
#y muestre un mensaje cada vez que un número no sea mayor que el anterior.

#> ejemplo:
#MAYORES QUE EL ANTERIOR
#¿Cuántos valores va a introducir? -1 ¡ Imposible!
for n in range(0):
	if numeros_a_introducir < 0:
		print("imposible")
#MAYORES QUE EL ANTERIOR
for i in range(numero_anterior - 1):
	escriba_num:str=input("escriba un numero: ")
if escriba_num >= 10:
	print(f"{escriba_num} no es mayor que 1")
if numero_anterior == escriba_num:
	print("gracias por su colaboracion")
#¿Cuántos valores va a introducir? 4
#Escriba un número: 6
#Escriba un número más grande que 6: 10
#Escriba un número más grande que 10: 8
#¡8 no es mayor que 10!
#Escriba un número más grande que 8: 9
#Gracias por su colaboración