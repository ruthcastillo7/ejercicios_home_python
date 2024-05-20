#*Ejercicio Ocho* (esta igual que el ejecicio 5)
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra:str=str(input("Introduce una palabra: "))
for i in range(len(palabra)-1,-1,-1):
		print(palabra[i])