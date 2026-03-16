import os
os.system('cls')

from Funcionario import Funcionario

class Principal:
    @staticmethod
    def main():
        func = Funcionario()

        func.cadastrarFunc()
        print(f'O aumento é: R$ {func.calcularAumento():.2f}')

if __name__ == '__main__':
    Principal.main()