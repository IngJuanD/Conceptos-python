lista=[]  # Declaramos la lista

for k in range(10):
	lista.append(input("Introduce un valor en lista: "))  # Añadimos los valores de la lista por teclado

print("Los elementos de la lista son: "+str(lista))  # Visualizamos los elementos de la lista
valor = int(input("Introduce el valor a modificar de la lista ingresa el indice: "))  # índice a modificar

nuevo = input ("Introduce el nuevo valor: ")  # Valor nuevo de índice que se modifica
lista[valor] = nuevo  # Hacemos la modificación
print("Los elementos de la lista son: "+str(lista)) # Visualizamos los elemntos para comprobar la modificación

valor=int(input("Introduce el índice en el que se insertará el nuevo valor: "))  # índice donde se inserta en nuevo valor
nuevo=input ("Introduce el nuevo valor: ") # Valor a insertar
lista.insert(valor, nuevo)

print("Los elementos de la lista son: "+str(lista)) # Visualizamos los elementos para comprobar la modificación
nuevo=input ("Introduce el valor a eliminar:") # Valor a eliminar
lista.remove(nuevo)   # Eliminamos el valor

print("Los elementos de la lista son: "+str(lista)) # Visualizamos lista
nuevo=input ("Introduce el valor a buscar: ")
resultado=(nuevo in lista)

if (resultado):
	print ("Existe este elemento y su índice es: "+str(lista.index(nuevo)))
else:
	print("No exite es elemento")






