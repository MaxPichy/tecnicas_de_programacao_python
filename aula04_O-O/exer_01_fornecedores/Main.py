import os
os.system('cls')

# Importar a classe Produto
from Fornecedores import Fornecedor

class Main:
    @staticmethod
    def main():
        fornecedor = Fornecedor()

        # Chamar os métodos
        fornecedor.cadastrarFornecedor()
        fornecedor.listarFornecedor()

if __name__ == '__main__':
    Main.main()