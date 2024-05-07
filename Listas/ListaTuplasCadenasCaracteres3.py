def meses_faltantes(inicio):
    meses=('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
    return meses[:inicio]


# Bloque principal
# Se recupera todos los meses anteriores a mes indicado
print("Imprimir los nombres de meses y todos los anteriores: ")
inicio = int(input("Ingrese el numero de mes: "))

mesesfalta = meses_faltantes(inicio)
print(mesesfalta)