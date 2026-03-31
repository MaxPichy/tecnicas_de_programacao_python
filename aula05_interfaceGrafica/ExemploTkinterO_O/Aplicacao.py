from tkinter import *

class Aplicacao:
  def __init__(self):
    self.tela = Tk()
    self.configurar_tela()
    self.criar_componentes()
  
  def configurar_tela(self):
    self.tela.title("Aplicação O.O.")
    self.tela.configure(background= "#1e3743")

    largura = 800
    altura = 300

    #PEGA A LARGURA E ALTURA DA TELA DO WINDOWS  
    largura_screen = self.tela.winfo_screenwidth()
    altura_Screen = self.tela.winfo_screenheight()

    #DEFINE O POSICIONAMENTO CENTRALIZADO
    posx = largura_screen / 2 - largura /2
    posy = altura_Screen / 2 - altura / 2

    #CONSTROI A TELA DE ACORDO COM AS DIMENSÕES DA TELA DO WINDONS
    #%d SUBSTIUI CADA NUMERO %CONCATENA CADA VARIAVEL
    self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
  
  def criar_componentes(self):
    self.txtnome = Entry(self.tela, width = 20, borderwidth = 3)
    self.txtnome.pack()

  def executar(self):
    self.tela.mainloop()