tupla = ("a","b","c","d")
tupla2 = 1,2,4,5,6
tupla_combinada = ("a",2,"f",4.4)

print(tupla_combinada)

print(tupla_combinada[0])

tupla_grande = ("Python","Java","C++","JavaScript","Cobol","Basic")

print(tupla_grande[2:5])

nueva_lista = list(tupla_combinada)
print(nueva_lista)

lista_orginal = [2,"dd",2,"f",6,9]
nueva_tupla = tuple(lista_orginal)
print(nueva_tupla)

tupla_letras = ("x","y","z")
for letra in tupla_letras:
    print(letra)

    