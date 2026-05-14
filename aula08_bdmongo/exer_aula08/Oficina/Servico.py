from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import pymongo
import sys
import itertools
from tkinter import ttk

class Servico:
    def __init__(self):
        self.tela = Tk()
        self.tela.geometry('800x600')
        self.tela.configure(background="#FC8E8E")
        
        self.tela.title('Oficina Relampago Marquinhos')
        
        #CRIAR BANCO DE DADOS MONGO
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        #CRIA BASE DE DADOS
        self.db = self.conexao["cadastro_servicos"]
        #CRIA COLEÇÃO
        self.collection = self.db["servicos"]
        
        self.criar_componentes()
        self.executar()
        
    def criar_componentes(self):
        Label(self.tela, text="Cadastro de Serviços",font=("Arial", 30, "bold"),bg="#FC8E8E", fg="black").place(x=200, y=50)

        Label(self.tela, text="Código:", bg="#FC8E8E", fg="black").place(x=200, y=110)
        self.txt_codigo = Entry(self.tela, width=20)
        self.txt_codigo.place(x=250, y=110)

        Label(self.tela, text="Serviço:", bg="#FC8E8E", fg="black").place(x=200, y=140)
        self.txt_servico = Entry(self.tela, width=20)
        self.txt_servico.place(x=250, y=140)

        Label(self.tela, text="Cliente:", bg="#FC8E8E", fg="black").place(x=200, y=170)
        self.txt_cliente = Entry(self.tela, width=20)
        self.txt_cliente.place(x=250, y=170)
        
        Label(self.tela, text="Data:", bg="#FC8E8E", fg="black").place(x=200, y=200)
        self.txt_data = Entry(self.tela, width=20)
        self.txt_data.place(x=250, y=200)

        Label(self.tela, text="Preço:", bg="#FC8E8E", fg="black").place(x=200, y=230)
        self.txt_preco = Entry(self.tela, width=20)
        self.txt_preco.place(x=250, y=230)
        
        Label(self.tela, text="Descrição:", bg="#FC8E8E", fg="black").place(x=480, y=110)
        self.txt_desc = scrolledtext.ScrolledText(self.tela, width=30, height=5, wrap=WORD)
        self.txt_desc.place(x=480, y=130)
        
        self.lbl_resultado = Label(self.tela, text="", bg="#FC8E8E", fg="black")
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
        
        self.relampago_img = PhotoImage(file='icones/rel_marquinhos.png')
        self.relampago = Label(self.tela, image=self.relampago_img, bg='#FC8E8E')
        self.relampago.place(x=245, y=400)
        
        try:
            self.katchau_gif = Image.open("icones/katchau.gif")
            tamanho = (150, 150)
            self.frames = []

            try:
                while True:
                    frame = self.katchau_gif.copy()
                    frame = frame.resize(tamanho, Image.Resampling.LANCZOS)
                    self.frames.append(ImageTk.PhotoImage(frame))
                    self.katchau_gif.seek(len(self.frames))
            except EOFError:
                pass
            
            if self.frames:
                self.katchau = Label(self.tela, bg='#FC8E8E')
                self.katchau.place(x=20, y=10) 
                
                self.frame_index = 0
                self.animar()  
            else:
                self.katchau = Label(self.tela, font=("Arial", 30), bg='#FC8E8E')
                self.katchau.place(x=50, y=50)
                
        except Exception as e:
            print(f"Erro ao carregar GIF: {e}")
        
    def animar(self):
        if hasattr(self, 'frames') and self.frames and hasattr(self, 'katchau'):
            self.katchau.config(image=self.frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            
            try:
                delay = self.katchau_gif.info().get('duration', 100)
            except:
                delay = 100 
            
            self.tela.after(delay, self.animar)
        
    def salvar(self):
        try:
            servico = {
                "codigo": self.txt_codigo.get(),
                "servico": self.txt_servico.get(),
                "cliente": self.txt_cliente.get(),
                "data": self.txt_data.get(),
                "preco": float(self.txt_preco.get()),
                "descricao": self.txt_desc.get("1.0", END).strip() 
            }

            self.collection.insert_one(servico)
            self.limpar()
            self.lbl_resultado.config(text="Salvo com sucesso!")

        except:
            self.lbl_resultado.config(text="Erro ao salvar")

    def atualizar(self):
        codigo = self.txt_codigo.get()

        self.collection.update_one(
            {"codigo": codigo},
            {"$set": {
                "servico": self.txt_servico.get(),
                "cliente": self.txt_cliente.get(),
                "data": self.txt_data.get(),
                "preco": float(self.txt_preco.get()),
                "descricao": self.txt_desc.get('1.0', END).strip()
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
            self.txt_servico.insert(END, resultado["servico"])
            self.txt_cliente.insert(END, resultado["cliente"])
            self.txt_data.insert(END, resultado["data"])
            self.txt_preco.insert(END, float(resultado["preco"]))
            self.txt_desc.insert('1.0', resultado["descricao"])
        else:
            self.lbl_resultado.config(text="Não encontrado")
            
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_servico.delete(0, END)
        self.txt_cliente.delete(0, END)
        self.txt_data.delete(0, END)
        self.txt_preco.delete(0, END)
        self.txt_desc.delete('1.0', END)

    def sair(self):
        sys.exit()
    
    def executar(self):
        self.tela.mainloop()