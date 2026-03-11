class Fornecedor:
    def __init__(self):
        self.__fornecedor = ''
        self.__produto = ''
        self.__descProduto = ''

    # Encapsulamento
    def get_Fornecedor(self):
        return self.__fornecedor
    def set_Fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    def get_Produto(self):
        return self.__produto
    def set_Produto(self, produto):
        self.__produto = produto

    def get_DescProduto(self):
        return self.__descProduto
    def set_DescProduto(self, descProduto):
        self.__descProduto = descProduto

    # Métodos
    def cadastrarFornecedor(self):
        print('\n ------- Cadastro de Fornecedores ------- \n')
        self.set_Fornecedor(input('Insira o nome do fornecedor: '))
        self.set_Produto(input('Insira o nome do produto: '))
        self.set_DescProduto(input('Insira a descrição do poduto: '))

    def listarFornecedor(self):
        print('\n ------- Dados do Fornecedor ------- \n')
        print('Fornecedor: ', self.get_Fornecedor())
        print('Produto: ', self.get_Produto())
        print('Descrição do Produto: ', self.get_DescProduto())