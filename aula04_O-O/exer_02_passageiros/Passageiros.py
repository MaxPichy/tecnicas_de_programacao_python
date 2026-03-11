class Passageiro:
    def __init__(self):
        self.__nome = ''
        self.__telefone = ''
        self.__rg = ''
        self.__local = '' 
        self.__data = ''
        self.__horario = ''
        self.__poltrona = ''

    # Encapsulamento
    def get_Nome(self):
        return self.__nome
    def set_Nome(self, nome):
        self.__nome = nome

    def get_Telefone(self):
        return self.__telefone
    def set_Telefone(self, telefone):
        self.__telefone = telefone

    def get_Rg(self):
        return self.__rg
    def set_Rg(self, rg):
        self.__rg = rg

    def get_Local(self):
        return self.__local
    def set_Local(self, local):
        self.__local = local

    def get_Data(self):
        return self.__data
    def set_Data(self, data):
        self.__data = data

    def get_Horario(self):
        return self.__horario
    def set_Horario(self, horario):
        self.__horario = horario

    def get_Poltrona(self):
        return self.__poltrona
    def set_Poltrona(self, poltrona):
        self.__poltrona = poltrona

    # Métodos
    def cadastrarPassageiro(self):
        print('\n ------- Cadastro de Passageiro ------- \n')
        self.set_Nome(input('Insira o nome: '))
        self.set_Telefone(input('Insira o telefone: '))
        self.set_Rg(input('Insira o RG: '))

    def mostrarPassageiro(self):
        print('\n ------- Listar de Passageiros ------- \n')
        print(f'Nome: {self.get_Nome()}')
        print(f'Telefone: {self.get_Telefone()}')
        print(f'RG: {self.get_Rg()}')

    def cadastrarPassagem(self):
        print('\n ------- Cadastro de Passagem ------- \n')
        self.set_Local(input('Insira o local: '))
        self.set_Data(input('Insira a data: '))
        self.set_Horario(input('Insira o horário: '))
        self.set_Poltrona(input('Insira o número da poltrona: '))

    def mostrarPassagem(self):
        print('\n ------- Listar Passagens ------- \n')
        print(f'Local: {self.get_Local()}')
        print(f'Data: {self.get_Data()}')
        print(f'Horário: {self.get_Horario()}')
        print(f'Poltrona: {self.get_Poltrona()}')
    