class Soma:
    def __init__(self):
      self.num1 = 0
      self.num2 = 0
      self.soma = 0

    def calcular(self):
      self.num1 = int(input('Digite o primeiro número: '))
      self.num2 = int(input('Digite o segundo número: '))
      self.soma = self.num1 + self.num2

      return print(f'Soma: {self.soma}')