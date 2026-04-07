class Contatos:
    def __init__(self):
        self.nome = ''
        self.telefone = ''
        self.endereco = ''
        self.cidade = ''

    def cadastrarDados(self):
        self.nome = input('Digite o nome: ')
        self.telefone = input('Digite o telefone: ')
        self.endereco = input('Digite o endereço: ')
        self.cidade = input('Digite a cidade: ')

    def mostrarDados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')
        print(f'Cidade: {self.cidade}')

