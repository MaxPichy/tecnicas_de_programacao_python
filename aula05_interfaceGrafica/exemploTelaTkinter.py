from tkinter import *
#Criando tela do Tkinter - Interface Grafica
tela = Tk()

#titulo
tela.title("Fatec Registro")

#cor de fundo
tela.configure(background="#3d3d3d")
#tamanho tela
tela.geometry("700x500")

#redimencionar tela true=habilitada / false = desabilitada
tela.resizable(True,True)
#redifine o tamanhp minimo e máximo para redimensionar
tela.minsize(width=400, height=600)
tela.maxsize(width=700, height=800)

#Criando Label
lbl_nome = Label(tela, text="Digite seu nome: ", background= "#ffffff" ,foreground= "#000000", font= "Arial 10 bold italic").place(x=10, y=20)
lbl_tel = Label(tela, text= "Digite seu telefone: ", background= "#ffffff", foreground= "#000000", font=("Arial", "10", "bold", "italic")).place(x=10, y=50)

#Criando caixa de texto
txt_nome = Entry(tela, width=50, borderwidth=3, bg="white", fg="black")
txt_nome.place(x=160, y=20)
txt_tel  = Entry(tela, width=50, borderwidth=3, bg="white", fg="black")
txt_tel.place(x=160, y=50)

def mostrardados():
  lbl_mostrar = Label(tela, text="Bem-vindo: "+ txt_nome.get()+ " - " + " Telefone: "+txt_tel.get())
  lbl_mostrar.place(x=100, y=150)

#Criando um botão
btn_botao = Button(tela, text="Mostrar Dados", command=mostrardados)
btn_botao.place(x = 160, y=100)

#executar tela
tela.mainloop()
