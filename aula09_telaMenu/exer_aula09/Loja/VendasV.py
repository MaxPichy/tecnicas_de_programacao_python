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

class VendasV:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Sistema de Vendas")
        self.tela.configure(bg="#410d63")

        self.largura = 900  
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
            self.cliente = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.cliente["loja"]
            self.collection = self.db["vendas"]
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
            text="Cadastro de Vendas",
            font=("Arial", 22, "bold"),
            bg="#410d63",
            fg="white"
        ).place(x=290, y=20)

        Label(self.tela, text="Código da Venda:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=90)
        Label(self.tela, text="Cliente:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=130)
        Label(self.tela, text="Produto:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=170)
        Label(self.tela, text="Quantidade:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=210)
        Label(self.tela, text="Preço Unitário:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=250)

        Label(self.tela, text="Total:", bg="#410d63", font=("Arial", 10, "bold"), fg="white").place(x=420, y=90)
        Label(self.tela, text="Pagamento:", bg="#410d63", font=("Arial", 10), fg="white").place(x=420, y=130)
        Label(self.tela, text="Vendedor:", bg="#410d63", font=("Arial", 10), fg="white").place(x=420, y=170)
        Label(self.tela, text="Observações:", bg="#410d63", font=("Arial", 10), fg="white").place(x=420, y=210)

        self.lbl_resultado = Label(self.tela, text="", bg="#410d63", font=("Arial", 10, "bold"), fg="white")
        self.lbl_resultado.place(x=300, y=430)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_codigo.place(x=180, y=90)
        
        self.txt_cliente = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_cliente.place(x=180, y=130)
        
        self.combo_produto = ttk.Combobox(self.tela, width=22, font=("Arial", 10))
        self.combo_produto['values'] = ('Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E')
        self.combo_produto.place(x=180, y=170)
        self.combo_produto.set("Selecione o produto")
        self.combo_produto.bind('<<ComboboxSelected>>', self.calcular_total)
        
        self.txt_quantidade = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_quantidade.place(x=180, y=210)
        self.txt_quantidade.bind('<KeyRelease>', self.calcular_total)
        
        self.txt_preco_unitario = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_preco_unitario.place(x=180, y=250)
        self.txt_preco_unitario.bind('<KeyRelease>', self.calcular_total)

        self.lbl_total = Label(self.tela, text="R$ 0.00", bg="#410d63", font=("Arial", 14, "bold"), fg="#00ff00")
        self.lbl_total.place(x=550, y=90)
        
        self.combo_pagamento = ttk.Combobox(self.tela, width=25, font=("Arial", 10))
        self.combo_pagamento['values'] = ('Dinheiro', 'Cartão de Crédito', 'Cartão de Débito', 'PIX', 'Boleto', 'Transferência')
        self.combo_pagamento.place(x=550, y=130)
        self.combo_pagamento.set('Selecione a forma')
        
        self.txt_vendedor = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_vendedor.place(x=550, y=170)
        
        self.txt_obs = scrolledtext.ScrolledText(self.tela, width=35, height=5, wrap=WORD, font=("Arial", 10))
        self.txt_obs.place(x=550, y=210)

    def calcular_total(self, event=None):
        try:
            quantidade = float(self.txt_quantidade.get()) if self.txt_quantidade.get() else 0
            preco = float(self.txt_preco_unitario.get()) if self.txt_preco_unitario.get() else 0
            total = quantidade * preco
            self.lbl_total.config(text=f"R$ {total:.2f}")
        except ValueError:
            self.lbl_total.config(text="R$ 0.00")

    # ICONES
    def criar_icones(self):
        try:
            self.foto_salvar = PhotoImage(file="icones/salvar.png")
            self.foto_alterar = PhotoImage(file="icones/alterar.png")
            self.foto_excluir = PhotoImage(file="icones/excluir.png")
            self.foto_consultar = PhotoImage(file="icones/consultar.png")
            self.foto_sair = PhotoImage(file="icones/sair.png")
        except:
            # Se não encontrar os ícones, cria botões sem ícones
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
        ).place(x=50, y=370)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP if self.foto_alterar else None,
            command=self.atualizar,
            width=80 if self.foto_alterar else 10,
            height=60 if self.foto_alterar else 2
        ).place(x=150, y=370)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP if self.foto_excluir else None,
            command=self.apagar,
            width=80 if self.foto_excluir else 10,
            height=60 if self.foto_excluir else 2
        ).place(x=250, y=370)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP if self.foto_consultar else None,
            command=self.consultar,
            width=80 if self.foto_consultar else 10,
            height=60 if self.foto_consultar else 2
        ).place(x=350, y=370)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP if self.foto_sair else None,
            command=self.sair,
            width=80 if self.foto_sair else 10,
            height=60 if self.foto_sair else 2
        ).place(x=550, y=370)
    
    # MÉTODOS   
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_cliente.delete(0, END)
        self.combo_produto.set("Selecione o produto")
        self.txt_quantidade.delete(0, END)
        self.txt_preco_unitario.delete(0, END)
        self.lbl_total.config(text="R$ 0.00")
        self.combo_pagamento.set("Selecione a forma")
        self.txt_vendedor.delete(0, END)
        self.txt_obs.delete('1.0', END)
        self.lbl_resultado.config(text="")
        self.txt_codigo.focus()

    def dados(self):
        try:
            quantidade = float(self.txt_quantidade.get()) if self.txt_quantidade.get() else 0
            preco = float(self.txt_preco_unitario.get()) if self.txt_preco_unitario.get() else 0
            total = quantidade * preco
        except ValueError:
            quantidade = 0
            preco = 0
            total = 0
            
        return {
            "codigo": self.txt_codigo.get(),
            "cliente": self.txt_cliente.get(),
            "produto": self.combo_produto.get(),
            "quantidade": quantidade,
            "preco_unitario": preco,
            "total": total,
            "forma_pagamento": self.combo_pagamento.get(),
            "vendedor": self.txt_vendedor.get(),
            "observacoes": self.txt_obs.get("1.0", END).strip(),
            "data_venda": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    def salvar(self):
        try:
            if not self.txt_codigo.get():
                messagebox.showwarning("Aviso", "O campo Código da Venda é obrigatório!")
                return
                
            if not self.txt_cliente.get():
                messagebox.showwarning("Aviso", "O campo Cliente é obrigatório!")
                return
                
            if self.combo_produto.get() == "Selecione o produto":
                messagebox.showwarning("Aviso", "Selecione um produto!")
                return
                
            if not self.txt_quantidade.get():
                messagebox.showwarning("Aviso", "Informe a quantidade!")
                return
                
            if not self.txt_preco_unitario.get():
                messagebox.showwarning("Aviso", "Informe o preço unitário!")
                return
                
            if self.combo_pagamento.get() == "Selecione a forma":
                messagebox.showwarning("Aviso", "Selecione a forma de pagamento!")
                return
                
            if self.collection.find_one({"codigo": self.txt_codigo.get()}):
                messagebox.showwarning("Aviso", "Já existe uma venda com este código!")
                return
                
            self.collection.insert_one(self.dados())
            self.limpar()
            self.lbl_resultado.config(text="✓ Venda salva com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Venda salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")

    def atualizar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código da venda!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Venda não encontrada!")
                return
                
            self.collection.update_one(
                {"codigo": codigo},
                {"$set": self.dados()}
            )
            
            self.lbl_resultado.config(text="✓ Venda atualizada com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Venda atualizada com sucesso!")
            self.limpar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

    def apagar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código da venda!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Venda não encontrada!")
                return
                
            resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir a venda {codigo}?")
            
            if resposta:
                self.collection.delete_one({"codigo": codigo})
                self.limpar()
                self.lbl_resultado.config(text="✓ Venda excluída com sucesso!", fg="green")
                messagebox.showinfo("Sucesso", "Venda excluída com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {str(e)}")

    def consultar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código da venda!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})

            if resultado:
                self.limpar()

                self.txt_codigo.insert(0, resultado.get("codigo", ""))
                self.txt_cliente.insert(0, resultado.get("cliente", ""))
                self.combo_produto.set(resultado.get("produto", ""))
                self.txt_quantidade.insert(0, str(resultado.get("quantidade", "")))
                self.txt_preco_unitario.insert(0, str(resultado.get("preco_unitario", "")))
                self.lbl_total.config(text=f"R$ {resultado.get('total', 0):.2f}")
                self.combo_pagamento.set(resultado.get("forma_pagamento", ""))
                self.txt_vendedor.insert(0, resultado.get("vendedor", ""))
                self.txt_obs.insert('1.0', resultado.get("observacoes", ""))
                
                self.lbl_resultado.config(text="✓ Venda encontrada!", fg="green")
            else:
                self.lbl_resultado.config(text="✗ Venda não encontrada!", fg="red")
                messagebox.showwarning("Aviso", "Venda não encontrada!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar: {str(e)}")
    
    def sair(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            self.tela.destroy()

# EXECUTAR
if __name__ == "__main__":
    VendasV()