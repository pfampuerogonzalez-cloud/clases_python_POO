
#clase persona tiene que ser en mayusculas y con la palabra reservada class

class Telefono:
 pass


class Persona:   #j     j     34
    def __init__(self,nombre,edad,rut):
        self.humano = True
        self.nombre = nombre
        self.edad = edad
        self.rut = rut

    def saludar(self):
        print(f"hola, mi nombre es: {self.nombre} y tengo {self.edad}")

    def cumplir_anios(self):
        self.edad +=1

    def verificar_rut(self):
       if self.rut == 0:
          print("sin rut")
       else:
            print("rut listo")
        

#instancia
juanito = Persona("juanito", 34, 1111111)
carlos = Persona("carlos", 32, 2222222)

#objeto
print(carlos.cumplir_anios())
print(carlos.verificar_rut())
print(carlos.saludar())

 