class Contato:
    def __init__(self):
        self.__nome = ''
        self.__telefone = ''
        self.__end = ''
        self.__cidade = ''

    # Encapsulamento
    def get_Nome(self):
        return self.__nome
    def set_Nome(self, nome):
        self.__nome = nome
    
    def get_Telefone(self):
        return self.__telefone
    def set_Telefone(self, telefone):
        self.__telefone = telefone

    def get_End(self):
        return self.__end
    def set_End(self, end):
        self.__end = end

    def get_Cidade(self):
        return self.__cidade
    def set_Cidade(self, cidade):
        self.__cidade = cidade

    # Métodos
    def cadastrarContato(self):
        print('\n ------- Cadastrar Contatos ------- \n')
        self.set_Nome(input('Insira o nome: '))
        self.set_Telefone(input('Insira o telefone: '))
        self.set_End(input('Insira o endereço: '))
        self.set_Cidade(input('Insira a cidade: '))

    def mostrarContato(self):
        print('\n ------- Listar Contato ------- \n')
        print(f'Nome: {self.get_Nome()}')
        print(f'Telefone: {self.get_Telefone()}')
        print(f'Endereço: {self.get_End()}')
        print(f'Cidade: {self.get_Cidade()}')