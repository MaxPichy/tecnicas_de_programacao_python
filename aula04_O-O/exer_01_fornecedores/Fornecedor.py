class Fornecedor:
    def __init__(self):
        self.__fornecedor = ''
        self.__produto = ''
        self.__descProduto = ''

    # Encapsulamento
    # Getter fornecedor
    def get_Fornecedor(self):
        return self.__fornecedor
    # Setter fornecedor
    def set_Fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    # Getter produto
    def get_Produto(self):
        return self.__produto
    # Setter produto
    def set_Produto(self, produto):
        self.__produto = produto

    # Getter descProduto
    def get_DescProduto(self):
        return self.__descProduto
    # Setter descProduto
    def set_DescProduto(self, descProduto):
        self.__descProduto = descProduto

    # Método: cadastrar
    def cadastrarFornecedor(self):
        print('\n === Cadastro de Fornecedores === \n')
        self.set_Fornecedor(input('Nome do Fornecedor: '))
        self.set_Produto(input('Nome do Produto: '))
        self.set_DescProduto(input('Descrição do Poduto: '))

    # Método: listar
    def listarFornecedor(self):
        print('\n === Dados do Fornecedor === \n')
        print('Fornecedor: ', self.get_Fornecedor())
        print('Produto: ', self.get_Produto())
        print('Descrição do Produto: ', self.get_DescProduto())