estudiante = {
    "nombre":"Juan",
    "apellido":"David",
    "edad":19,
    "ciudad":"Paris"

}

print(estudiante["nombre"])
estudiante["edad"] = 21
print(estudiante)

estudiante["cursos"] = ["Python","Java","C#"]
print(estudiante)

for llave in estudiante:
    print(llave)

for llave in estudiante:
    print(estudiante[llave])


for llave,valor in estudiante.items():
    print(llave,valor)