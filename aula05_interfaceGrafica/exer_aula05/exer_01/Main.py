from Clientes import Clientes

class Main:
    @staticmethod
    def main():
        cli = Clientes()
        cli.mostrarDados()
        cli.cadastrarCliente()

if __name__ == '__main__':
    Main.main()