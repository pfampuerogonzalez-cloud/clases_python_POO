
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
        

#instancia
juanito = Persona("juanito", 34, 1111111)
carlos = Persona("carlos", 32, 2222222)

#objeto
print(carlos.saludar())


