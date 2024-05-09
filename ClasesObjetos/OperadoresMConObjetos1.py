#Operadores Matematicos
class Operadores:

    def __init__(self, lista):
        self.lista = lista

    def visualizar(self):
        print(self.lista)

    def __add__(self,entero): #Suma
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x] + entero)
        return nueva

    def __sub__(self,entero): #Resta
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x] - entero)
        return nueva

    def __mul__(self,entero): #Multiplicacion
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x] * entero)
        return nueva

    def __floordiv__(self,entero):
        nueva = []
        for x in range(len(self.lista)):
            nueva.append(self.lista[x] / entero)
        return nueva
    

# Bloque principal

datos = Operadores([20,25,82])
datos.visualizar()
print(datos+2)
print(datos-2)
print(datos*2)
print(datos//2)