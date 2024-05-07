def meses_faltantes(numero):
    meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

    return meses[numero:]


# Bloque principal
#Se recupera desde el mes indicado hasta el final de la lista

print("Imprimir los nombres de meses que faltan hasta fin de año")
numero = int(input("Ingrese el numero de mes: "))
mesesfalta = meses_faltantes(numero)
print(mesesfalta)