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

class ClientesV:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Sistema de Clientes")
        self.tela.configure(bg="#410d63")

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
            self.cliente = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.cliente["loja"]
            self.collection = self.db["clientes"]
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
            text="Cadastro de Clientes",
            font=("Arial", 22, "bold"),
            bg="#410d63",
            fg="white"
        ).place(x=280, y=20)

        Label(self.tela, text="Código:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=90)
        Label(self.tela, text="Nome Completo:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=130)
        Label(self.tela, text="Email:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=170)
        Label(self.tela, text="Telefone:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=210)
        Label(self.tela, text="Data Nascimento:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=250)
    
        Label(self.tela, text="CPF/CNPJ:", bg="#410d63", font=("Arial", 10), fg="white").place(x=470, y=90)
        Label(self.tela, text="Logradouro:", bg="#410d63", font=("Arial", 10), fg="white").place(x=470, y=130)
        Label(self.tela, text="Bairro:", bg="#410d63", font=("Arial", 10), fg="white").place(x=470, y=170)
        Label(self.tela, text="Cidade:", bg="#410d63", font=("Arial", 10), fg="white").place(x=470, y=210)
        Label(self.tela, text="Estado:", bg="#410d63", font=("Arial", 10), fg="white").place(x=470, y=250)

        self.lbl_resultado = Label(self.tela, text="", bg="#410d63", font=("Arial", 10, "bold"), fg="white")
        self.lbl_resultado.place(x=300, y=480)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_codigo.place(x=200, y=90)
        
        self.txt_nome = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_nome.place(x=200, y=130)
        
        self.txt_email = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_email.place(x=200, y=170)
        
        self.txt_telefone = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_telefone.place(x=200, y=210)
        
        self.txt_data_nasc = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_data_nasc.place(x=200, y=250)
        self.txt_data_nasc.insert(0, "DD/MM/AAAA")
        self.txt_data_nasc.bind('<FocusIn>', self.limpar_placeholder_data)
        self.txt_data_nasc.bind('<FocusOut>', self.restaurar_placeholder_data)

        self.txt_cpf_cnpj = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_cpf_cnpj.place(x=580, y=90)
        
        self.txt_logradouro = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_logradouro.place(x=580, y=130)
        
        self.txt_bairro = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_bairro.place(x=580, y=170)
        
        self.txt_cidade = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_cidade.place(x=580, y=210)
        
        self.combo_estado = ttk.Combobox(
            self.tela,
            values=[
                "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
                "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
                "RS", "RO", "RR", "SC", "SP", "SE", "TO"
            ],
            width=22,
            font=("Arial", 10)
        )
        self.combo_estado.place(x=580, y=250)
        self.combo_estado.set("Selecione o estado")

    def limpar_placeholder_data(self, event):
        if self.txt_data_nasc.get() == "DD/MM/AAAA":
            self.txt_data_nasc.delete(0, END)
    
    def restaurar_placeholder_data(self, event):
        if not self.txt_data_nasc.get():
            self.txt_data_nasc.insert(0, "DD/MM/AAAA")

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
            compound=TOP if self.foto_salvar else None,
            command=self.salvar,
            width=80 if self.foto_salvar else 10,
            height=60 if self.foto_salvar else 2
        ).place(x=50, y=380)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP if self.foto_alterar else None,
            command=self.atualizar,
            width=80 if self.foto_alterar else 10,
            height=60 if self.foto_alterar else 2
        ).place(x=150, y=380)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP if self.foto_excluir else None,
            command=self.apagar,
            width=80 if self.foto_excluir else 10,
            height=60 if self.foto_excluir else 2
        ).place(x=250, y=380)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP if self.foto_consultar else None,
            command=self.consultar,
            width=80 if self.foto_consultar else 10,
            height=60 if self.foto_consultar else 2
        ).place(x=350, y=380)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP if self.foto_sair else None,
            command=self.sair,
            width=80 if self.foto_sair else 10,
            height=60 if self.foto_sair else 2
        ).place(x=600, y=400)

    # MÉTODOS   
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_data_nasc.delete(0, END)
        self.txt_data_nasc.insert(0, "DD/MM/AAAA")
        self.txt_cpf_cnpj.delete(0, END)
        self.txt_logradouro.delete(0, END)
        self.txt_bairro.delete(0, END)
        self.txt_cidade.delete(0, END)
        self.combo_estado.set("Selecione o estado")
        self.lbl_resultado.config(text="")
        self.txt_codigo.focus()

    def dados(self):
        # Validação de idade
        idade = None
        data_nasc = self.txt_data_nasc.get()
        if data_nasc and data_nasc != "DD/MM/AAAA":
            try:
                data_nasc_obj = datetime.strptime(data_nasc, "%d/%m/%Y")
                hoje = datetime.now()
                idade = hoje.year - data_nasc_obj.year - ((hoje.month, hoje.day) < (data_nasc_obj.month, data_nasc_obj.day))
            except:
                idade = None
                
        return {
            "codigo": self.txt_codigo.get(),
            "nome": self.txt_nome.get(),
            "email": self.txt_email.get(),
            "telefone": self.txt_telefone.get(),
            "data_nascimento": data_nasc if data_nasc != "DD/MM/AAAA" else "",
            "idade": idade,
            "cpf_cnpj": self.txt_cpf_cnpj.get(),
            "logradouro": self.txt_logradouro.get(),
            "bairro": self.txt_bairro.get(),
            "cidade": self.txt_cidade.get(),
            "estado": self.combo_estado.get(),
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
                
            if not self.txt_cpf_cnpj.get():
                messagebox.showwarning("Aviso", "O campo CPF/CNPJ é obrigatório!")
                return
                
            if self.collection.find_one({"codigo": self.txt_codigo.get()}):
                messagebox.showwarning("Aviso", "Já existe um cliente com este código!")
                return
                
            if self.collection.find_one({"cpf_cnpj": self.txt_cpf_cnpj.get()}):
                messagebox.showwarning("Aviso", "Já existe um cliente com este CPF/CNPJ!")
                return
                
            self.collection.insert_one(self.dados())
            self.limpar()
            self.lbl_resultado.config(text="✓ Cliente salvo com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")

    def atualizar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do cliente!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Cliente não encontrado!")
                return
                
            # Verificar se o CPF/CNPJ já existe em outro cliente
            cpf_cnpj = self.txt_cpf_cnpj.get()
            outro_cliente = self.collection.find_one({
                "cpf_cnpj": cpf_cnpj,
                "codigo": {"$ne": codigo}
            })
            
            if outro_cliente:
                messagebox.showwarning("Aviso", "Este CPF/CNPJ já está cadastrado para outro cliente!")
                return
                
            self.collection.update_one(
                {"codigo": codigo},
                {"$set": self.dados()}
            )
            
            self.lbl_resultado.config(text="✓ Cliente atualizado com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            self.limpar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

    def apagar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do cliente!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Cliente não encontrado!")
                return
                
            resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o cliente {codigo} - {resultado.get('nome', '')}?")
            
            if resposta:
                self.collection.delete_one({"codigo": codigo})
                self.limpar()
                self.lbl_resultado.config(text="✓ Cliente excluído com sucesso!", fg="green")
                messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {str(e)}")

    def consultar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do cliente!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})

            if resultado:
                self.limpar()

                self.txt_codigo.insert(0, resultado.get("codigo", ""))
                self.txt_nome.insert(0, resultado.get("nome", ""))
                self.txt_email.insert(0, resultado.get("email", ""))
                self.txt_telefone.insert(0, resultado.get("telefone", ""))
                
                data_nasc = resultado.get("data_nascimento", "")
                if data_nasc:
                    self.txt_data_nasc.delete(0, END)
                    self.txt_data_nasc.insert(0, data_nasc)
                else:
                    self.txt_data_nasc.insert(0, "DD/MM/AAAA")
                    
                self.txt_cpf_cnpj.insert(0, resultado.get("cpf_cnpj", ""))
                self.txt_logradouro.insert(0, resultado.get("logradouro", ""))
                self.txt_bairro.insert(0, resultado.get("bairro", ""))
                self.txt_cidade.insert(0, resultado.get("cidade", ""))
                self.combo_estado.set(resultado.get("estado", "Selecione o estado"))
                
                self.lbl_resultado.config(text="✓ Cliente encontrado!", fg="green")
            else:
                self.lbl_resultado.config(text="✗ Cliente não encontrado!", fg="red")
                messagebox.showwarning("Aviso", "Cliente não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar: {str(e)}")
    
    def sair(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            self.tela.destroy()

# EXECUTAR
if __name__ == "__main__":
    ClientesV()