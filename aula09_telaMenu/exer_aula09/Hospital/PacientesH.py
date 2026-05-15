from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sys
import os
from datetime import datetime

try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo

class PacientesH:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Pacientes")
        self.tela.configure(bg="#afcfe4")

        self.largura = 900  
        self.altura = 550  

        self.centralizar_tela()
        self.conectar_banco()
        self.criar_componentes()

        self.tela.mainloop()
  
    # CRIANDO TELA
    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = int(largura_screen / 2 - self.largura / 2)
        posy = int(altura_screen / 2 - self.altura / 2)

        self.tela.geometry(f"{self.largura}x{self.altura}+{posx}+{posy}")
        self.tela.resizable(False, False)  
    
    # CRIAR BANCO
    def conectar_banco(self):
        try:
            self.paciente = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.paciente["hospital"]
            self.collection = self.db["pacientes"]
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco: {str(e)}")
    
    # COMPONENTES    
    def criar_componentes(self):
        self.criar_labels()
        self.criar_campos()
        self.criar_icones()
        self.criar_botoes()

    def criar_labels(self):
        Label(
            self.tela,
            text="Cadastro de Pacientes",
            font=("Arial", 22, "bold"),
            bg="#afcfe4"
        ).place(x=250, y=20)

        Label(self.tela, text="Código:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=90)
        Label(self.tela, text="Nome:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=130)
        Label(self.tela, text="Idade:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=170)
        Label(self.tela, text="Bairro:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=210)
    
        Label(self.tela, text="CPF:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=90)
        Label(self.tela, text="Rua:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=130)
        Label(self.tela, text="Cidade:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=170)
        Label(self.tela, text="Estado:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=210)

        self.lbl_resultado = Label(self.tela, text="", bg="#afcfe4", font=("Arial", 10, "bold"))
        self.lbl_resultado.place(x=300, y=480)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_codigo.place(x=160, y=90)
        
        self.txt_nome = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_nome.place(x=160, y=130)
        
        self.txt_idade = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_idade.place(x=160, y=170)
        
        self.txt_bairro = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_bairro.place(x=160, y=210)

        self.txt_cpf = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_cpf.place(x=520, y=90)
        
        self.txt_end = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_end.place(x=520, y=130)
        
        self.txt_cidade = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_cidade.place(x=520, y=170)
        
        self.comboestado = ttk.Combobox(
            self.tela,
            values=[
                "São Paulo",
                "Rio de Janeiro",
                "Minas Gerais",
                "Espírito Santo",
                "Bahia",
                "Paraná",
                "Rio Grande do Sul",
                "Santa Catarina",
                "Goiás",
                "Pernambuco"
            ],
            width=22,
            font=("Arial", 10)
        )
        self.comboestado.place(x=520, y=210)
        self.comboestado.set("Selecione o estado")

    # ICONES
    def criar_icones(self):
        try:
            self.foto_salvar = PhotoImage(file="icones/salvar.png")
            self.foto_alterar = PhotoImage(file="icones/alterar.png")
            self.foto_excluir = PhotoImage(file="icones/excluir.png")
            self.foto_consultar = PhotoImage(file="icones/consultar.png")
            self.foto_sair = PhotoImage(file="icones/sair.png")
        except Exception as e:
            print(f"Erro ao carregar ícones: {e}")
            self.foto_salvar = None
            self.foto_alterar = None
            self.foto_excluir = None
            self.foto_consultar = None
            self.foto_sair = None

    # BOTOES
    def criar_botoes(self):
        Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            command=self.salvar,
            width=80,
            height=60
        ).place(x=50, y=380)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            command=self.atualizar,
            width=80,
            height=60
        ).place(x=150, y=380)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            command=self.apagar,
            width=80,
            height=60
        ).place(x=250, y=380)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            command=self.consultar,
            width=80,
            height=60
        ).place(x=350, y=380)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            command=self.sair,
            width=80,
            height=60
        ).place(x=600, y=400)

    # MÉTODOS   
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_cpf.delete(0, END)
        self.txt_idade.delete(0, END)
        self.txt_end.delete(0, END)
        self.txt_bairro.delete(0, END)
        self.txt_cidade.delete(0, END)
        self.comboestado.set("Selecione o estado")
        self.lbl_resultado.config(text="")
        self.txt_codigo.focus()

    def dados(self):
        return {
            "codigo": self.txt_codigo.get(),
            "nome": self.txt_nome.get(),
            "cpf": self.txt_cpf.get(),
            "idade": self.txt_idade.get(),  
            "endereco": self.txt_end.get(),
            "bairro": self.txt_bairro.get(),
            "cidade": self.txt_cidade.get(),
            "estado": self.comboestado.get(),
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def salvar(self):
        try:
            if not self.txt_codigo.get():
                messagebox.showwarning("Aviso", "O campo Código é obrigatório!")
                return
                
            if not self.txt_nome.get():
                messagebox.showwarning("Aviso", "O campo Nome é obrigatório!")
                return
                
            if self.collection.find_one({"codigo": self.txt_codigo.get()}):
                messagebox.showwarning("Aviso", "Já existe um paciente com este código!")
                return
                
            self.collection.insert_one(self.dados())
            self.limpar()
            self.lbl_resultado.config(text="✓ Paciente salvo com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Paciente salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")

    def atualizar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do paciente!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Paciente não encontrado!")
                return
                
            self.collection.update_one(
                {"codigo": codigo},
                {"$set": self.dados()}
            )
            
            self.lbl_resultado.config(text="✓ Paciente atualizado com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso!")
            self.limpar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

    def apagar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do paciente!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Paciente não encontrado!")
                return
                
            resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o paciente {codigo}?")
            
            if resposta:
                self.collection.delete_one({"codigo": codigo})
                self.limpar()
                self.lbl_resultado.config(text="✓ Paciente excluído com sucesso!", fg="green")
                messagebox.showinfo("Sucesso", "Paciente excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {str(e)}")

    def consultar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do paciente!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})

            if resultado:
                self.limpar()

                self.txt_codigo.insert(0, resultado.get("codigo", ""))
                self.txt_nome.insert(0, resultado.get("nome", ""))
                self.txt_cpf.insert(0, resultado.get("cpf", ""))
                self.txt_idade.insert(0, resultado.get("idade", ""))
                self.txt_end.insert(0, resultado.get("endereco", ""))
                self.txt_bairro.insert(0, resultado.get("bairro", ""))
                self.txt_cidade.insert(0, resultado.get("cidade", ""))
                self.comboestado.set(resultado.get("estado", "Selecione o estado"))
                
                self.lbl_resultado.config(text="✓ Paciente encontrado!", fg="green")
            else:
                self.lbl_resultado.config(text="✗ Paciente não encontrado!", fg="red")
                messagebox.showwarning("Aviso", "Paciente não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar: {str(e)}")
    
    def sair(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            self.tela.destroy()

# EXECUTAR
if __name__ == "__main__":
    PacientesH()