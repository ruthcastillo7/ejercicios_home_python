# *Ejercicio Diez*
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
palabra:str=str(input("Introduce una palabra: "))
letra:str=str(input("Introduce una letra: "))
contador = 0
for n in palabra:
	if n == letra:
		contador=contador+1
print(f"La letra '{letra}' aparece {contador} veces en la frase.")