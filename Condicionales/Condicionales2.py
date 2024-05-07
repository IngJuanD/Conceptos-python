# utilizamos función input para introducir valores por teclado
sueldo=int(input("Introduce el sueldo: "))

# codicional if 
if sueldo>3000:
	print("El usuario debe pagar un porcentage en impuestos")

if sueldo<=3000:  #Operador de comparación
    print("El usuario esta exento de declarar su renta")

if sueldo>6000 and sueldo<10000: # Operador lógico se tiene que cumplir las dos condiciones
    print("El usuario tiene que pagar una bonificación de 1000 COP")

if sueldo == 20000 or sueldo == 30000: #Operador lógico sólo se tiene que cumplir una de las dos condiciones
    print("El usuario paga un 10% de su sueldo")	
