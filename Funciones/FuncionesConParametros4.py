 #EJEMPLO 2 RETORNO DE DATOS
#Retorno de datos se devuelven a la llamada de la función que recoge los datos
def retorno_superficie(lado):
	sup = lado * lado
	return sup  #Con la instrucción return se retorna los datos de la función

va = int(input("Introduce el valor del cuadrado: "))
superficie = retorno_superficie(va) # Aqui recogemos los datos que enviamos y lo almacenamos en la variable superficie
print("El cuadrado del numero es:", superficie)	
