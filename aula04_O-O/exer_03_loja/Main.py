import os
os.system('cls')

from Lojas import Loja

class Main:
    @staticmethod
    def main():
        loja = Loja()

        #Chamar os métodos
        loja.inserirLoja()
        loja.inserirCompra()

        loja.mostrarLoja()
        loja.mostrarCompra()
        loja.calcularCompra()

if __name__ == '__main__':
    Main.main()


        