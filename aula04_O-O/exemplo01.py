# Cliar classe Carro

class Carro:
    # Construtor da classe
    def __init__(self, nome):
        self.nome = nome

    # Método da classe Carro
    def acelerar(self):
        print(self.nome, "está acelerando...")

# Instanciando o objeto car da classe Carro
car = Carro("Impala 67")
print(car.nome)
car.acelerar()

c = Carro("Uno")
print(c.nome)
c.acelerar()