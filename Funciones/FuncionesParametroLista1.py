def sumarDeValores(lista):
	suma = 0
	for x in range(len(lista)):
		suma = suma + lista[x]

	return suma

def ValorMayor(lista):
	may = lista[0]
	for x in range(1,len(lista)):
		if lista[x] > may:
			may = lista[x]

	return may

def ValorMenor(lista):
	men = lista[0]
	for x in range(1, len(lista)):
		if lista[x] < men:
			men = lista[x]
			
	return men

datos=[5454, 43430, 3222, 12222, 666, 65656, 545, 2333, 21212, 23, 6565]
print("Total de datos: ") 
print(datos)

print("El total de sumar los valores del array: ", sumarDeValores(datos))
print("Valor mayor del array: ", ValorMayor(datos)) 
print("Valor menor del array: ", ValorMenor(datos)) 
"""Creamos un array con varios valores numéricos, para que nuestra función pueda operar con ellos sólo 
tenemos que enviarselos cuando hacemos la llamada a la función entre los paréntesis  
introducimos el nombre de nuestra array, con esto ya estamos enviando los datos a la función.
para recuperar esos valores en la función ponemos un parámetro, con esto la función identifica 
los valores que va a recoger y ya podemos operar con ellos dentro de la función"""

