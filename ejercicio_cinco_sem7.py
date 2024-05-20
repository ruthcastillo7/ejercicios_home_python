#*Ejercicio Cinco*
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

usuario:str=str(input("querido usuario ingrese una palabra: "))
for i in range(len(usuario)-1,-1,-1):
		print(usuario[i])