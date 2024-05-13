#Cambiar sentido a lista
lista  = ["g","f","e","d","c","b","a"]
nueva_lista = []
nueva_lista2 = []

for indice in range(len(lista)-1,-1,-1):
    nueva_lista.append(lista[indice])

print(nueva_lista)

for letra in reversed(lista):
    nueva_lista2.append(letra)
print(nueva_lista2)
