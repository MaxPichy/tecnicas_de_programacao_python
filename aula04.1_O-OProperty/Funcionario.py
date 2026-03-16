class Funcionario:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__salAtual = 0.0
        self.__salAumento = 0.0

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _idade(self):
        return self.__idade

    @_idade.setter
    def _idade(self, value):
        self.__idade = value

    @property
    def _salAtual(self):
        return self.__salAtual

    @_salAtual.setter
    def _salAtual(self, value):
        self.__salAtual = value

    @property
    def _salAumento(self):
        return self.__salAumento

    @_salAumento.setter
    def _salAumento(self, value):
        self.__salAumento = value


    def cadastrarFunc(self):
        self.__nome = input('Digite o nome: ')
        self.__idade = int(input('Digite a idade: '))
        self.__salAtual = float(input('Digite salário atual: '))

    def calcularAumento(self):
        self.__salAumento = self._salAtual + (self._salAtual * 10)/100
        return self.__salAumento


        