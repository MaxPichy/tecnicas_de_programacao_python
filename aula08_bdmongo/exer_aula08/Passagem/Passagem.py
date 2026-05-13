from tkinter import *
import pymongo
import sys
from tkinter import ttk

class Passagem:
    def __init__(self):
        self.tela = Tk()
        self.tela.geometry('800x600')
        self.tela.configure(background="#51182f")
        
        self.tela.title('Cadastro de Passagens')
        
        #CRIAR BANCO DE DADOS MONGO
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        #CRIA BASE DE DADOS
        self.db = self.conexao["cadastro_passagens"]
        #CRIA COLEÇÃO
        self.collection = self.db["passagem"]
        
        self.criar_componentes()
        self.executar()
        
    def criar_componentes(self):
        Label(self.tela, text="Cadastro de Passagens",font=("Arial", 30, "bold"),bg="#51182f", fg="white").place(x=200, y=50)

        Label(self.tela, text="Código:", bg="#51182f", fg="white").place(x=130, y=110)
        self.txt_codigo = Entry(self.tela, width=20)
        self.txt_codigo.place(x=190, y=110)

        Label(self.tela, text="Nome:", bg="#51182f", fg="white").place(x=130, y=140)
        self.txt_nome = Entry(self.tela, width=20)
        self.txt_nome.place(x=190, y=140)

        Label(self.tela, text="Telefone:", bg="#51182f", fg="white").place(x=130, y=170)
        self.txt_telefone = Entry(self.tela, width=20)
        self.txt_telefone.place(x=190, y=170)

        Label(self.tela, text="RG:", bg="#51182f", fg="white").place(x=450, y=170)
        self.txt_rg = Entry(self.tela, width=20)
        self.txt_rg.place(x=480, y=170)

        Label(self.tela, text="Local:", bg="#51182f", fg="white").place(x=130, y=200)
        self.txt_local = Entry(self.tela, width=20)
        self.txt_local.place(x=190, y=200)

        Label(self.tela, text="Data:", bg="#51182f", fg="white").place(x=445, y=200)
        self.txt_data = Entry(self.tela, width=20)
        self.txt_data.place(x=480, y=200)

        Label(self.tela, text="Horário:", bg="#51182f", fg="white").place(x=130, y=230)
        self.txt_horario = Entry(self.tela, width=20)
        self.txt_horario.place(x=190, y=230)

        Label(self.tela, text="N° Poltrona:", bg="#51182f", fg="white").place(x=430, y=230)
        self.txt_poltrona = Entry(self.tela, width=20)
        self.txt_poltrona.place(x=500, y=230)

        self.lbl_resultado = Label(self.tela, text="", bg="#51182f", fg="white")
        self.lbl_resultado.place(x=490, y=410)

        #CRIANDO OS BOTÕES     
        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")
   
        self.btn_salvar = Button(self.tela, text="Salvar",image=self.foto_salvar,compound=TOP,command=self.salvar)
        self.btn_salvar.place(x=130, y=280)

        self.btn_excluir = Button(self.tela, text="Excluir",image=self.foto_excluir,compound=TOP,command=self.excluir)
        self.btn_excluir.place(x=220, y=280)
        
        self.btn_alterar = Button(self.tela, text="Alterar",image=self.foto_alterar,compound=TOP,command=self.atualizar)
        self.btn_alterar.place(x=310, y=280)

        self.btn_consultar = Button(self.tela, text="Consultar",image=self.foto_consultar,compound=TOP,command=self.consultar)        
        self.btn_consultar.place(x=400, y=280)

        self.btn_sair = Button(self.tela, text="Sair",image=self.foto_sair,compound=RIGHT,command=self.sair)  
        self.btn_sair.place(x=490, y=280)
        
    def salvar(self):
        try:
            passagem = {
                "codigo": self.txt_codigo.get(),
                "nome": self.txt_nome.get(),
                "telefone": self.txt_telefone.get(),
                "rg": self.txt_rg.get(),
                "local": self.txt_local.get(),
                "horario": self.txt_horario.get(),
                "data": self.txt_data.get(),
                "poltrona": self.txt_poltrona.get()
            }

            self.collection.insert_one(passagem)
            self.limpar()
            self.lbl_resultado.config(text="Salvo com sucesso!")

        except:
            self.lbl_resultado.config(text="Erro ao salvar")

    def atualizar(self):
        codigo = self.txt_codigo.get()

        self.collection.update_one(
            {"codigo": codigo},
            {"$set": {
                "nome": self.txt_nome.get(),
                "telefone": self.txt_telefone.get(),
                "rg": self.txt_rg.get(),
                "local": self.txt_local.get(),
                "horario": self.txt_horario.get(),
                "data": self.txt_data.get(),
                "poltrona": self.txt_poltrona.get()
            }}
        )

        self.limpar()
        self.lbl_resultado.config(text="Atualizado!")
        
    def excluir(self):
        codigo = self.txt_codigo.get()
        self.collection.delete_one({"codigo": codigo})
        self.limpar()
        self.lbl_resultado.config(text="Excluído!")

    def consultar(self):
     
        codigo = self.txt_codigo.get()

        resultado = self.collection.find_one({"codigo": codigo})

        if resultado:
            self.txt_nome.insert(END, resultado["nome"])
            self.txt_telefone.insert(END, resultado["telefone"])
            self.txt_rg.insert(END, resultado["rg"])
            self.txt_local.insert(END, resultado["local"])
            self.txt_horario.insert(END, resultado["horario"])
            self.txt_data.insert(END, resultado["data"])
            self.txt_poltrona.insert(END, resultado["poltrona"])
        else:
            self.lbl_resultado.config(text="Não encontrado")
            
    def limpar(self):
        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_rg.delete(0, END)
        self.txt_local.delete(0, END)
        self.txt_horario.delete(0, END)
        self.txt_data.delete(0, END)
        self.txt_poltrona.delete(0, END)

    def sair(self):
        sys.exit()
    
    def executar(self):
        self.tela.mainloop()