import os
os.system('cls')

from Medias import Media

class Main:
    @staticmethod
    def main():
        media = Media()

        #Chamar os métodos
        media.set_Aluno()
        media.inserirNotas()
        media.calcularMedia()
        media.mostrarNomeMedia()

if __name__ == '__main__':
    Main.main()