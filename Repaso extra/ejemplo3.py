directorio_direcciones = {
    "Elena" : "Roma 123, Italia",
    "Vilma" : "Paris 22A, Francia",
    "Pablo" : "Malaga 89, España"
}

print(directorio_direcciones["Pablo"])
print(directorio_direcciones.get("Ana","Persona no encontrada en el directorio"))

directorio_buscar = "Paris 22A, Francia"

if (directorio_buscar in directorio_direcciones.values()):
    for persona,direccion in directorio_direcciones.items():
        if(directorio_buscar == direccion):
            print(persona)
else:
    print("No existe la direccion indicada")