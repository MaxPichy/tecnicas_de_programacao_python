from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk, messagebox
import tkinter as tk
import sys
import os

try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo

class TratamentosH:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Tratamentos")
        self.tela.configure(bg="#afcfe4")

        self.largura = 800 
        self.altura = 500

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
            self.Tratamento = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.Tratamento["hospital"]
            self.collection = self.db["tratamentos"]
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
            text="Cadastro de Tratamentos",
            font=("Arial", 22, "bold"),
            bg="#afcfe4"
        ).place(x=250, y=20)

        Label(self.tela, text="Código:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=100)
        Label(self.tela, text="Paciente:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=140)
        Label(self.tela, text="Diagnóstico:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=180)
        Label(self.tela, text="Data de Início:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=220)
        Label(self.tela, text="Data de Término:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=260)

        Label(self.tela, text="Médico:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=100)
        Label(self.tela, text="Status:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=140)
        Label(self.tela, text="Descrição:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=180)

        self.lbl_resultado = Label(self.tela, text="", bg="#afcfe4", font=("Arial", 10, "bold"))
        self.lbl_resultado.place(x=300, y=430)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_codigo.place(x=160, y=100)
        
        self.txt_paciente = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_paciente.place(x=160, y=140)
        
        self.txt_diagnostico = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_diagnostico.place(x=160, y=180)
        
        self.txt_data_inicio = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_data_inicio.place(x=160, y=220)
        
        self.txt_data_termino = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_data_termino.place(x=160, y=260)

        self.txt_medico = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_medico.place(x=520, y=100)
        
        self.combo_status = ttk.Combobox(self.tela, width=22, font=("Arial", 10))
        self.combo_status['values'] = ('Em andamento', 'Concluído', 'Interrompido', 'Aguardando')
        self.combo_status.place(x=520, y=140)
        self.combo_status.set('Em andamento')
        
        self.txt_desc = scrolledtext.ScrolledText(self.tela, width=30, height=4, wrap=WORD, font=("Arial", 10))
        self.txt_desc.place(x=520, y=180)

    # ICONES
    def criar_icones(self):
        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

    # BOTOES
    def criar_botoes(self):
        btn_salvar = Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            command=self.salvar,
            width=80,
            height=60
        )
        btn_salvar.place(x=50, y=370)

        btn_alterar = Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            command=self.atualizar,
            width=80,
            height=60
        )
        btn_alterar.place(x=150, y=370)

        btn_excluir = Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            command=self.apagar,
            width=80,
            height=60
        )
        btn_excluir.place(x=250, y=370)

        btn_consultar = Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            command=self.consultar,
            width=80,
            height=60
        )
        btn_consultar.place(x=350, y=370)

        btn_sair = Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            command=self.sair,
            width=80,
            height=60
        )
        btn_sair.place(x=550, y=370)

    # MÉTODOS   
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_paciente.delete(0, END)
        self.txt_medico.delete(0, END)
        self.txt_diagnostico.delete(0, END)
        self.txt_data_inicio.delete(0, END)
        self.txt_data_termino.delete(0, END)
        self.txt_desc.delete('1.0', END)
        self.combo_status.set('Em andamento')
        self.lbl_resultado.config(text="")
        self.txt_codigo.focus()

    def dados(self):
        return {
            "codigo": self.txt_codigo.get(),
            "paciente": self.txt_paciente.get(),
            "medico": self.txt_medico.get(),
            "diagnostico": self.txt_diagnostico.get(),
            "data_inicio": self.txt_data_inicio.get(),
            "data_termino": self.txt_data_termino.get(),
            "status": self.combo_status.get(),
            "descricao": self.txt_desc.get("1.0", END).strip()
        }

    def salvar(self):
        try:
            if not self.txt_codigo.get():
                messagebox.showwarning("Aviso", "O campo Código é obrigatório!")
                return
                
            if self.collection.find_one({"codigo": self.txt_codigo.get()}):
                messagebox.showwarning("Aviso", "Já existe um tratamento com este código!")
                return
                
            self.collection.insert_one(self.dados())
            self.limpar()
            self.lbl_resultado.config(text="✓ Tratamento salvo com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Tratamento salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")

    def atualizar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do tratamento!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Tratamento não encontrado!")
                return
                
            self.collection.update_one(
                {"codigo": codigo},
                {"$set": self.dados()}
            )
            
            self.lbl_resultado.config(text="✓ Tratamento atualizado com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Tratamento atualizado com sucesso!")
            self.limpar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

    def apagar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do tratamento!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Tratamento não encontrado!")
                return
                
            resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o tratamento {codigo}?")
            
            if resposta:
                self.collection.delete_one({"codigo": codigo})
                self.limpar()
                self.lbl_resultado.config(text="✓ Tratamento excluído com sucesso!", fg="green")
                messagebox.showinfo("Sucesso", "Tratamento excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {str(e)}")

    def consultar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do tratamento!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})

            if resultado:
                self.limpar()

                self.txt_codigo.insert(0, resultado.get("codigo", ""))
                self.txt_paciente.insert(0, resultado.get("paciente", ""))
                self.txt_medico.insert(0, resultado.get("medico", ""))
                self.txt_diagnostico.insert(0, resultado.get("diagnostico", ""))
                self.txt_data_inicio.insert(0, resultado.get("data_inicio", ""))
                self.txt_data_termino.insert(0, resultado.get("data_termino", ""))
                self.combo_status.set(resultado.get("status", "Em andamento"))
                self.txt_desc.insert('1.0', resultado.get("descricao", ""))
                
                self.lbl_resultado.config(text="✓ Tratamento encontrado!", fg="green")
            else:
                self.lbl_resultado.config(text="✗ Tratamento não encontrado!", fg="red")
                messagebox.showwarning("Aviso", "Tratamento não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar: {str(e)}")
    
    def sair(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            self.tela.destroy()

# EXECUTAR
if __name__ == "__main__":
    TratamentosH()