from tkinter import *
from tkinter import scrolledtext
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

class ConsultasH:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Consultas")
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
            self.Consulta = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.Consulta["hospital"]
            self.collection = self.db["consultas"]
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
            text="Cadastro de Consultas Médicas",
            font=("Arial", 22, "bold"),
            bg="#afcfe4"
        ).place(x=250, y=20)

        Label(self.tela, text="Código:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=90)
        Label(self.tela, text="Paciente:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=130)
        Label(self.tela, text="Médico:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=170)
        Label(self.tela, text="Data:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=210)
        Label(self.tela, text="Hora:", bg="#afcfe4", font=("Arial", 10)).place(x=50, y=250)

        Label(self.tela, text="Tipo:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=90)
        Label(self.tela, text="Status:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=130)
        Label(self.tela, text="Descrição:", bg="#afcfe4", font=("Arial", 10)).place(x=420, y=170)

        self.lbl_resultado = Label(self.tela, text="", bg="#afcfe4", font=("Arial", 10, "bold"))
        self.lbl_resultado.place(x=300, y=430)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_codigo.place(x=160, y=90)
        
        self.txt_paciente = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_paciente.place(x=160, y=130)
        
        self.txt_medico = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_medico.place(x=160, y=170)
        
        self.txt_data = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_data.place(x=160, y=210)
        self.txt_data.insert(0, "DD/MM/AAAA")
        self.txt_data.bind('<FocusIn>', self.limpar_placeholder_data)
        self.txt_data.bind('<FocusOut>', self.restaurar_placeholder_data)
        
        self.combo_hora = ttk.Combobox(self.tela, width=22, font=("Arial", 10))
        horas = [f"{h:02d}:{m:02d}" for h in range(8, 19) for m in (0, 30)]
        self.combo_hora['values'] = horas
        self.combo_hora.place(x=160, y=250)
        self.combo_hora.set("Selecione a hora")

        self.combo_tipo = ttk.Combobox(self.tela, width=25, font=("Arial", 10))
        self.combo_tipo['values'] = ('Consulta inicial', 'Retorno', 'Emergência', 'Teleconsulta')
        self.combo_tipo.place(x=520, y=90)
        self.combo_tipo.set('Selecione o tipo')
        
        self.combo_status = ttk.Combobox(self.tela, width=25, font=("Arial", 10))
        self.combo_status['values'] = ('Agendada', 'Realizada', 'Cancelada', 'Pendente')
        self.combo_status.place(x=520, y=130)
        self.combo_status.set('Agendada')
        
        self.txt_desc = scrolledtext.ScrolledText(self.tela, width=35, height=5, wrap=WORD, font=("Arial", 10))
        self.txt_desc.place(x=520, y=170)

    def limpar_placeholder_data(self, event):
        if self.txt_data.get() == "DD/MM/AAAA":
            self.txt_data.delete(0, END)
    
    def restaurar_placeholder_data(self, event):
        if not self.txt_data.get():
            self.txt_data.insert(0, "DD/MM/AAAA")

    # ICONES
    def criar_icones(self):
        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

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
        ).place(x=50, y=370)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            command=self.atualizar,
            width=80,
            height=60
        ).place(x=150, y=370)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            command=self.apagar,
            width=80,
            height=60
        ).place(x=250, y=370)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            command=self.consultar,
            width=80,
            height=60
        ).place(x=350, y=370)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            command=self.sair,
            width=80,
            height=60
        ).place(x=550, y=370)
    
    # MÉTODOS   
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_paciente.delete(0, END)
        self.txt_medico.delete(0, END)
        self.txt_data.delete(0, END)
        self.txt_data.insert(0, "DD/MM/AAAA")
        self.combo_hora.set("Selecione a hora")
        self.combo_tipo.set("Selecione o tipo")
        self.combo_status.set("Agendada")
        self.txt_desc.delete('1.0', END)
        self.lbl_resultado.config(text="")
        self.txt_codigo.focus()

    def dados(self):
        return {
            "codigo": self.txt_codigo.get(),
            "paciente": self.txt_paciente.get(),
            "medico": self.txt_medico.get(),
            "data": self.txt_data.get(),
            "hora": self.combo_hora.get(),
            "tipo": self.combo_tipo.get(),
            "status": self.combo_status.get(),
            "descricao": self.txt_desc.get("1.0", END).strip(),
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def salvar(self):
        try:
            if not self.txt_codigo.get():
                messagebox.showwarning("Aviso", "O campo Código é obrigatório!")
                return
                
            if not self.txt_paciente.get():
                messagebox.showwarning("Aviso", "O campo Paciente é obrigatório!")
                return
                
            if not self.txt_medico.get():
                messagebox.showwarning("Aviso", "O campo Médico é obrigatório!")
                return
                
            if self.collection.find_one({"codigo": self.txt_codigo.get()}):
                messagebox.showwarning("Aviso", "Já existe uma consulta com este código!")
                return
                
            self.collection.insert_one(self.dados())
            self.limpar()
            self.lbl_resultado.config(text="✓ Consulta salva com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Consulta salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")

    def atualizar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código da consulta!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Consulta não encontrada!")
                return
                
            self.collection.update_one(
                {"codigo": codigo},
                {"$set": self.dados()}
            )
            
            self.lbl_resultado.config(text="✓ Consulta atualizada com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Consulta atualizada com sucesso!")
            self.limpar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

    def apagar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código da consulta!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Consulta não encontrada!")
                return
                
            resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir a consulta {codigo}?")
            
            if resposta:
                self.collection.delete_one({"codigo": codigo})
                self.limpar()
                self.lbl_resultado.config(text="✓ Consulta excluída com sucesso!", fg="green")
                messagebox.showinfo("Sucesso", "Consulta excluída com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {str(e)}")

    def consultar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código da consulta!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})

            if resultado:
                self.limpar()

                self.txt_codigo.insert(0, resultado.get("codigo", ""))
                self.txt_paciente.insert(0, resultado.get("paciente", ""))
                self.txt_medico.insert(0, resultado.get("medico", ""))
                self.txt_data.insert(0, resultado.get("data", ""))
                self.combo_hora.set(resultado.get("hora", ""))
                self.combo_tipo.set(resultado.get("tipo", ""))
                self.combo_status.set(resultado.get("status", "Agendada"))
                self.txt_desc.insert('1.0', resultado.get("descricao", ""))
                
                self.lbl_resultado.config(text="✓ Consulta encontrada!", fg="green")
            else:
                self.lbl_resultado.config(text="✗ Consulta não encontrada!", fg="red")
                messagebox.showwarning("Aviso", "Consulta não encontrada!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar: {str(e)}")
    
    def sair(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            self.tela.destroy()

# EXECUTAR
if __name__ == "__main__":
    ConsultasH()