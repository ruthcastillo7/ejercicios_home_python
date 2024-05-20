# *Ejercicio Once*
# Escriba un programa que pregunte cuantos números se van a introducir
numero:str=int(input("¿cuantos numeros introducirá?: "))
# pida los esos números (que puedan ser decimales)
numero_pedido:str=float(input("introduce numero (puede ser decimal): "))
#y calcule su suma, mostrar por terminal la suma de los números introducidos.
suma=numero+numero_pedido
print(f"La suma de los números introducidos es: {numero} + {numero_pedido} =", suma)