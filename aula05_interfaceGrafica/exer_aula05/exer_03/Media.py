class Media:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.media = 0

    def calcular(self):
        self.n1 = float(input('Digite a primeira nota: '))
        self.n2 = float(input('Digite a segunda nota: '))
        self.n3 = float(input('Digite a terceira nota: '))

        self.media = float((self.n1 + self.n2 + self.n3) / 3)

        if(self.media >= 7):
            print(f'Média: {self.media:.2f}')
            print('Aprovado')
        elif(self.media <= 3):
            print(f'Média: {self.media:.2f}')
            print('Reprovado')
        else:
            print(f'Média: {self.media:.2f}')
            print('Exame')