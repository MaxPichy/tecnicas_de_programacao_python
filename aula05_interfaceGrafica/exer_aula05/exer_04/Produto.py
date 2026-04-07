class Produto:
    def __init__(self):
        self.nome = ''
        self.quantidade = 0
        self.valor = 0
        self.total = 0
    
    def calcular(self):
        self.nome = input('Digite o produto: ')
        self.quantidade = int(input('Digite a quantidade: '))
        self.valor = float(input('Digite o valor: '))
        
        self.total = self.valor * self.quantidade
    
    def mostrarDadosProduto(self):
        print(f'Nome: {self.nome}')
        print(f'Quantidade: {self.quantidade}')
        print(f'Valor: {self.valor}')
        print(f'Total: {self.total:.2f}')