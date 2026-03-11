class Media:
    def __init__(self):
        self.__aluno = ''
        self.__nota1 = 0
        self.__nota2 = 0
        self.__media = 0
    
    # Encapsulamento
    def get_Aluno(self):
        return self.__aluno
    def set_Aluno(self, aluno):
        self.__aluno = aluno

    def get_Nota1(self):
        return self.__nota1
    def set_Nota1(self, nota1):
        self.__nota1 = nota1

    def get_Nota2(self):
        return self.__nota2
    def set_Nota2(self, nota2):
        self.__nota2 = nota2

    def set_Media(self, media):
        self.__media = media

    # Métodos
    def inserirNotas(self):
        self.set_Nota1(input('Insira a Nota 1: '))
        self.set_Nota2(input('Insira a Nota 2: '))
    
    def calcularMedia(self):
        nota1 = float(self.get_Nota1)
        nota2 = float(self.get_Nota2)
        self.set_Media = nota1 * nota2
    
    def mostrarNomeMedia(self):
        print(f'\n ------- Dados ------- \n')
        print('Nome: ', self.__aluno)
        print(f'Média: {self.calcularMedia():.2f}')