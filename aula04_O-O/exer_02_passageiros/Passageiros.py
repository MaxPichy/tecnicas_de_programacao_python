class Passageiros:
    def __init__(self):
        self.__nome = ''
        self.__telefone = ''
        self.__rg = ''
        self.__local = '' 
        self.__data = ''
        self.__horario = ''
        self.__poltrona = ''

    def get_Nome(self):
        return self.__nome
    def set_Nome(self, nome):
        self.__nome = nome

    