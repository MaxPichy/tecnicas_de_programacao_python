from tkinter import *
import pymongo
import sys
from tkinter import ttk

class Produto:
    def __init__(self):
        self.tela = Tk()
        self.tela.geometry('800x600')
        self.tela.configure(background="#9ef1de")
        
        self.tela.title('Cadastro de Produtos')
        
        self.conexao = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.conexao['cadastro_produtos']
        self.collection = self.db['produtos']
        
        self.criar_componentes()
        self.executar()
        
    def criar_componentes(self):
        Label(self.tela, text = 'Cadastro de Produtos', font=("Arial", 30, "bold"),bg="#9ef1de").place(x=200, y=50)
        
        # Inputs
        Label(self.tela, text="Código:", bg="#9ef1de").place(x=130, y=140)
        self.txt_codigo = Entry(self.tela, width=20)
        self.txt_codigo.place(x=190, y=140)
        
        Label(self.tela, text="Nome:", bg="#9ef1de").place(x=130, y=170)
        self.txt_nome = Entry(self.tela, width=40)
        self.txt_nome.place(x=190, y=170)

        Label(self.tela, text="Quantidade:", bg="#9ef1de").place(x=450, y=170)
        self.txt_qtd = Entry(self.tela, width=20)
        self.txt_qtd.place(x=530, y=170)
        self.txt_qtd.bind('<KeyRelease>', self.calcular_total)

        Label(self.tela, text="Preço:", bg="#9ef1de").place(x=130, y=200)
        self.txt_preco = Entry(self.tela, width=20)
        self.txt_preco.place(x=190, y=200)
        self.txt_preco.bind('<KeyRelease>', self.calcular_total)

        Label(self.tela, text="Total:", bg="#9ef1de").place(x=450, y=200)
        self.txt_total = Entry(self.tela, width=25, state='readonly')
        self.txt_total.place(x=490, y=200)
        
        self.lbl_resultado = Label(self.tela, text='', bg='#9ef1de')
        self.lbl_resultado.place(x=490, y=410)
        
        # Botões
        self.foto_cadastrar = PhotoImage(file="icones/salvar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")
        
        self.btn_cadastrar = Button(self.tela, text="Cadastrar",image=self.foto_cadastrar,compound=TOP,command=self.cadastrar)
        self.btn_cadastrar.place(x=130, y=280)

        self.btn_excluir = Button(self.tela, text="Excluir",image=self.foto_excluir,compound=TOP,command=self.excluir)
        self.btn_excluir.place(x=220, y=280)
        
        self.btn_alterar = Button(self.tela, text="Alterar",image=self.foto_alterar,compound=TOP,command=self.alterar)
        self.btn_alterar.place(x=310, y=280)

        self.btn_consultar = Button(self.tela, text="Consultar",image=self.foto_consultar,compound=TOP,command=self.consultar)        
        self.btn_consultar.place(x=400, y=280)

        self.btn_sair = Button(self.tela, text="Sair",image=self.foto_sair,compound=RIGHT,command=self.sair)  
        self.btn_sair.place(x=490, y=280)
    
    def calcular_total(self, event = None):
        qtd = int(self.txt_qtd.get())
        preco = float(self.txt_preco.get())
        total = qtd * preco
        
        self.txt_total.config(state='normal')
        self.txt_total.delete(0, END)
        self.txt_total.insert(0, f"{total:.2f}")
        self.txt_total.config(state='readonly')
                
        return total
    
    def cadastrar(self):       
        total = self.calcular_total()
        
        try:
            produto = {
                "codigo": int(self.txt_codigo.get()),
                "nome": self.txt_nome.get(),
                "quantidade": int(self.txt_qtd.get()),
                "preco": float(self.txt_preco.get()),
                "total": total,
            }

            self.collection.insert_one(produto)
            self.limpar()
            self.lbl_resultado.config(text="Salvo com sucesso!")

        except:
            self.lbl_resultado.config(text="Erro ao salvar")
            
    def alterar(self):
        codigo = int(self.txt_codigo.get())
        total = self.calcular_total()
        
        self.limpar()

        self.collection.update_one(
            {"codigo": codigo},
            {"$set": {
                "nome": self.txt_nome.get(),
                "quantidade": int(self.txt_qtd.get()),
                "preco": float(self.txt_preco.get()),
                "total": total,
            }}
        )

        self.lbl_resultado.config(text="Atualizado!")
        
    def excluir(self):
        codigo = int(self.txt_codigo.get())
        
        self.collection.delete_one({"codigo": codigo})
        self.limpar()
        self.lbl_resultado.config(text="Excluído!")
        
    def consultar(self):
        codigo = int(self.txt_codigo.get())
        resultado = self.collection.find_one({"codigo": codigo})
        
        self.limpar()

        if resultado:
            self.txt_nome.insert(END, resultado["nome"])
            self.txt_qtd.insert(END, resultado["quantidade"])
            self.txt_preco.insert(END, f"{resultado['preco']:.2f}")
            self.txt_total.insert(0, f"{self.calcular_total():.2f}")
            self.txt_total.config(state='readonly')
        else:
            self.lbl_resultado.config(text="Não encontrado")
        
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_qtd.delete(0, END)
        self.txt_preco.delete(0, END)
        self.txt_total.delete(0, END)
        
    def sair(self):
        sys.exit()
    
    def executar(self):
        self.tela.mainloop()