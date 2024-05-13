lista  = [1,4]
lista.append(33)
print(lista)
lista.extend([3,4,5])

lista.insert(1,2)#indice, valor

letras = ["x","y","z"]
letras.remove("y") #Valor

nombres = ["Juan","Pedro","Ana"]
nombres.pop()#Eliminar el ultimo elemento

nombres.pop(1)#(Indice)

numeros = [1,2,2,2,3,4,5,6]
print(numeros.count(2))

print(numeros.index(4))#Retorna posicion en la lista

print(len(numeros))
