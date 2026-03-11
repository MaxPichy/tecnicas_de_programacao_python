import os
os.system('cls')

from Contatos import Contato

class Main:
    @staticmethod
    def main():
        contato = Contato()

        #Chamar os métodos
        contato.cadastrarContato()
        contato.mostrarContato()

if __name__ == '__main__':
    Main.main()
