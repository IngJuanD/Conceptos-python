# EJEMPLO 1 PARAMETROS
def mostrar_mensaje(mensaje):
	#Funciones con parámetros simple
	print("*************************************")
	print(mensaje)
	print("*************************************")

def cargar_suma():
	valor1=int(input("Ingresa el primer valor: "))
	valor2=int(input("Ingresa el segundo valor: "))

	suma=valor1+valor2
	
	print("La suma es:",suma)


mostrar_mensaje("Calculo de suma de dos valores")
cargar_suma()



