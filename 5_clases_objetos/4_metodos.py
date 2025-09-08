class Contador:
    # Atributo de clase para contar instancias
    contadores_creados = 0
    
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial
        Contador.contadores_creados +=1

    def incrementar(self):
        self.valor +=1
        return self.valor 
    
    def decrementar(self):
        if self.valor == 0:
            return "El contador no puede ser negativo"
        else:
            self.valor -= 1
            return self.valor
    
    @classmethod 
    def reiniciar_contador_global(cls):
        Contador.contadores_creados = 0

    @staticmethod
    def es_par(numero):
        return True if numero %2 == 0 else False


c1 = Contador(5)
c2 = Contador(7)

print(c1.incrementar())
print(c2.incrementar())
print(c1.decrementar() )     
print(c2.decrementar())
Contador.reiniciar_contador_global()
print(c1.es_par(5))
