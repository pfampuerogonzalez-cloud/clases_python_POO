
#PILARES DE LA POO


#ENCAPSULACIÓN

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo #SE PUEDE ENCAPSULAR CON __ 2 BARRAS PARA OCULTAR METODOS O ATRIBUTOS

   #ESTO CAMBIA EL NOMBRE DEL OBJETO DE ESTO: <__main__.CuentaBancaria object at 0x748e3e1ffb00>
   #A ESTO: esto es el objeto : {self.titular} y tiene un saldo de {self.saldo}

    def __str__(self):
       return f"esto es el objeto : {self.titular} y tiene un saldo de {self.__saldo}"

    def __depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    
    def retirar(self,monto):
        if monto < self.__saldo:
            self.__saldo -= monto
        else:
            print("retiro no es posible, trabaje más")

cuenta1 = CuentaBancaria("juanito", 10000)
cuenta2 = CuentaBancaria("Marcela", 100)

#ESTO ES EL OBJETO <__main__.CuentaBancaria object at 0x748e3e1ffb00>
#cuenta1.retirar(10000)
#cuenta1.__depositar(1000)
#print(cuenta1)




#HERENCIA

class Vehiculo:
    def __init__(self,marca,cant_ruedas):
        self.marca = marca
        self.cant_ruedas = cant_ruedas
        

    def moverse(self):
        print("auto se movio!!")

class Auto(Vehiculo): 
    def moverse(self):
        print ("auto moviendose")

class Moto(Vehiculo):
    def moverse(self):
        print("moto moviendose")

auto = Auto("byd")
moto = Moto("ktm")

auto.moverse()
moto.moverse()
      