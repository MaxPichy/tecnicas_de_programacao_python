import os
os.system('cls')

from Passageiros import Passageiro

class Main:
    @staticmethod
    def main():
        passageiros = Passageiro()

        # Chamar os métodos
        passageiros.cadastrarPassageiro()
        passageiros.cadastrarPassagem()

        passageiros.mostrarPassageiro()
        passageiros.mostrarPassagem()

if __name__ == '__main__':
    Main.main()