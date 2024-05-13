#Sumatoria de una lista
lista = [2,4,6,3,2]
sumatoria = 0

for numero in lista:
    sumatoria += numero

print(sumatoria)

#Promedio de una lista
promedio = 0
for num in lista:
    promedio += num

promedio /= len(lista)
print(promedio)


#maximo y minimo
max = 0
for num in lista:
    if max < num:
        max = num
print(max)

lista_negativa = [-1,-2,-5,-8]
max = lista_negativa[0]
for num in lista_negativa:
    if max < num:
        max = num
print(max)

min = lista_negativa[0]
for num in lista_negativa:
    if min > num:
        min = num
print(min)
