class Loja:
    def __init__(self):
        self.__razaoSocial = ''
        self.__cliCpf = ''
        self.__valorCompra = 0.0
        self.__qtdItens = 0

    # Encapsulamento
    def get_RazaoSocial(self):
        return self.__razaoSocial
    def set_RazaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial
    
    def get_CliCpf(self):
        return self.__cliCpf
    def set_CliCpf(self, cliCpf):
        self.__cliCpf = cliCpf

    def get_ValorCompra(self):
        return self.__valorCompra
    def set_ValorCompra(self, valorCompra):
        self.__valorCompra = valorCompra

    def get_QtdItens(self):
        return self.__qtdItens
    def set_QtdItens(self, qtdItens):
        self.__qtdItens = qtdItens

    # Métodos
    def inserirLoja(self):
        print('\n ------- Cadastro de Lojas ------- \n')
        self.set_RazaoSocial(input('Insira a razão social: '))

    def mostrarLoja(self):
        print('\n ------- Listar Loja ------- \n')
        print(f'Razão Social: {self.get_RazaoSocial()}')

    def inserirCompra(self):
        print('\n ------- Compras ------- \n')
        self.set_CliCpf(input('Insira o CPF do cliente: '))
        self.set_QtdItens(input('Insira a quantidade de itens: '))
        self.set_ValorCompra(input('Insira o valor unitário: '))

    def mostrarCompra(self):
        print('\n ------- Listar Compra ------- \n')
        print(f'CPF do Cliente: {self.get_CliCpf()}')
        print(f'Quantidade de Itens: {self.get_QtdItens()}')
        print(f'Valor Unitário: R$ {self.get_ValorCompra()}')

    def calcularCompra(self):
        qtd = float(self.get_QtdItens())
        valorCompra = float(self.get_ValorCompra())
        valorTotal = qtd * valorCompra
        print(f'Valor Total: R$ {valorTotal:.2f}')