lenguajes1 = {"Python","C++","Java"}
lenguajes2 = {"Cobot1","Java","C#"}

todos_lenguajes = lenguajes1.union(lenguajes2)
print(todos_lenguajes)

coincidencia = lenguajes1.intersection(lenguajes2)
print(coincidencia)

print(lenguajes1.isdisjoint(lenguajes2))

mas_lenguaje = {"Javascript","Swift"}

print(lenguajes1.isdisjoint(mas_lenguaje))

diferencias = lenguajes1.difference(lenguajes2)
print(diferencias)