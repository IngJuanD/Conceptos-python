class Alumno:
    def declarar(Self,nombre,dato):
        Self.nombre = nombre
        Self.puntuacion = dato

    def visualizar(self):
        print("Nombre: ",self.nombre)
        print("Puntuacion: ",self.puntuacion)

    def estadistica(self):
        if self.puntuacion <= 3:
            print("Insuficiente")
        elif self.puntuacion >= 3.2:
            print("Notable")
        elif self.puntuacion >= 4:
            print("sobresaliente")
        else:
            print("Libre")
        
#Bloque principal

alumno1 = Alumno()
alumno1.declarar("David",4)
alumno1.visualizar()
alumno1.estadistica()

alumno2 = Alumno()
alumno2.declarar("Sofia",2)
alumno2.visualizar()
alumno2.estadistica()