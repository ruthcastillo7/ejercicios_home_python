# *Ejercicio Siete*
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase:str=str(input("escribe una frase: "))
contador:int=0
for n in range(0,len(frase)):
	if frase [n]=="a":
		contador+=1
		print(f"la letra a parece {contador} veces en la frase {frase}")