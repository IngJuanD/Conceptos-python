lista_alumnos = [
    {"Nombre":"Vilma","Apellido":"Mesa","id":123,"Cursos":["HTML","Python"]},
    {"Nombre":"Juana","Apellido":"De Arco","id":124,"Cursos":["HTML","Python","MERN"]},
    {"Nombre":"Pedro","Apellido":"Montes","id":134,"Cursos":["HTML","Python","MERN"]}
]

lista_alumnos[2]["Cursos"].pop(2)

from pprint import pprint

pprint(lista_alumnos)