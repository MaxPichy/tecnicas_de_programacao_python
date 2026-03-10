class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    # Método: mostrar infos de produtos
    def mostrar(self):
        print('Nome: ', self.nome)
        print(f'Preço: R$ {self.preco:.2f}')
        print(f'Quantidade: {self.qtd}')

    # Método: calcular valor total
    def calcularTotal(self):
        valor = float(self.preco * self.qtd)
        print(f'Valor Total: R$ {valor:.2f}')

# Instanciar um objeto e chamar os métodos da classe
prod = Produto('Abacate', 4.9, 3)
prod.mostrar()
prod.calcularTotal()