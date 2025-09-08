class Vehiculo:
    def __init__(self, marca,modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    

    def mostrar_info(self):
        return f"Vehiculo marca: {self.marca}, modelo: {self.modelo} año:{self.año}"
    
class Automovil(Vehiculo):
    def __init__(self, marca,modelo, año,puertas):
        super().__init__(marca,modelo, año)
        self.puertas = puertas
    
    def mostrar_info(self):
        return super().mostrar_info() + f" numero de puertas: {self.puertas}"
    
class Motocicleta(Vehiculo):
    def __init__(self, marca,modelo, año,cilindrada ): 
        super().__init__(marca,modelo, año)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        return super().mostrar_info() + f" cilindraje: {self.cilindrada}"
    
auto = Automovil("Toyota","Corolla","2016","5")
print(auto.mostrar_info())
moto = Motocicleta("Harley","Davison","1900",2000)
print(moto.mostrar_info())