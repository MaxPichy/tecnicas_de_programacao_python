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

class ProdutosV:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Sistema de Produtos")
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
            self.collection = self.db["produtos"]
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
            text="Cadastro de Produtos",
            font=("Arial", 22, "bold"),
            bg="#410d63",
            fg="white"
        ).place(x=280, y=20)

        Label(self.tela, text="Código:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=100)
        Label(self.tela, text="Nome:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=140)
        Label(self.tela, text="Categoria:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=180)
        Label(self.tela, text="Quantidade:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=220)
        Label(self.tela, text="Preço:", bg="#410d63", font=("Arial", 10), fg="white").place(x=50, y=260)

        Label(self.tela, text="Fornecedor:", bg="#410d63", font=("Arial", 10), fg="white").place(x=420, y=100)
        Label(self.tela, text="Estoque Mínimo:", bg="#410d63", font=("Arial", 10), fg="white").place(x=420, y=140)
        Label(self.tela, text="Localização:", bg="#410d63", font=("Arial", 10), fg="white").place(x=420, y=180)
        Label(self.tela, text="Descrição:", bg="#410d63", font=("Arial", 10), fg="white").place(x=420, y=220)

        self.lbl_resultado = Label(self.tela, text="", bg="#410d63", font=("Arial", 10, "bold"), fg="white")
        self.lbl_resultado.place(x=300, y=430)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_codigo.place(x=160, y=100)
        
        self.txt_nome = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_nome.place(x=160, y=140)
        
        self.combo_categoria = ttk.Combobox(self.tela, width=22, font=("Arial", 10))
        self.combo_categoria['values'] = ('Eletrônicos', 'Roupas', 'Alimentos', 'Móveis', 'Livros', 'Brinquedos', 'Esportes', 'Outros')
        self.combo_categoria.place(x=160, y=180)
        self.combo_categoria.set('Eletrônicos')
        
        self.txt_quantidade = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_quantidade.place(x=160, y=220)
        
        self.txt_preco = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_preco.place(x=160, y=260)

        self.txt_fornecedor = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_fornecedor.place(x=540, y=100)
        
        self.txt_estoque_minimo = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_estoque_minimo.place(x=540, y=140)
        
        self.txt_localizacao = Entry(self.tela, width=25, font=("Arial", 10))
        self.txt_localizacao.place(x=540, y=180)
        
        self.txt_desc = scrolledtext.ScrolledText(self.tela, width=30, height=4, wrap=WORD, font=("Arial", 10))
        self.txt_desc.place(x=540, y=220)

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
        btn_salvar = Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP if self.foto_salvar else None,
            command=self.salvar,
            width=80 if self.foto_salvar else 10,
            height=60 if self.foto_salvar else 2
        )
        btn_salvar.place(x=50, y=370)

        btn_alterar = Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP if self.foto_alterar else None,
            command=self.atualizar,
            width=80 if self.foto_alterar else 10,
            height=60 if self.foto_alterar else 2
        )
        btn_alterar.place(x=150, y=370)

        btn_excluir = Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP if self.foto_excluir else None,
            command=self.apagar,
            width=80 if self.foto_excluir else 10,
            height=60 if self.foto_excluir else 2
        )
        btn_excluir.place(x=250, y=370)

        btn_consultar = Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP if self.foto_consultar else None,
            command=self.consultar,
            width=80 if self.foto_consultar else 10,
            height=60 if self.foto_consultar else 2
        )
        btn_consultar.place(x=350, y=370)

        btn_sair = Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP if self.foto_sair else None,
            command=self.sair,
            width=80 if self.foto_sair else 10,
            height=60 if self.foto_sair else 2
        )
        btn_sair.place(x=550, y=370)

    # MÉTODOS   
    def limpar(self):
        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_quantidade.delete(0, END)
        self.txt_preco.delete(0, END)
        self.txt_fornecedor.delete(0, END)
        self.txt_estoque_minimo.delete(0, END)
        self.txt_localizacao.delete(0, END)
        self.txt_desc.delete('1.0', END)
        self.combo_categoria.set('Eletrônicos')
        self.lbl_resultado.config(text="")
        self.txt_codigo.focus()

    def dados(self):
        return {
            "codigo": self.txt_codigo.get(),
            "nome": self.txt_nome.get(),
            "categoria": self.combo_categoria.get(),
            "quantidade": int(self.txt_quantidade.get()) if self.txt_quantidade.get().isdigit() else 0,
            "preco": float(self.txt_preco.get()) if self.txt_preco.get().replace('.', '').isdigit() else 0.0,
            "fornecedor": self.txt_fornecedor.get(),
            "estoque_minimo": int(self.txt_estoque_minimo.get()) if self.txt_estoque_minimo.get().isdigit() else 0,
            "localizacao": self.txt_localizacao.get(),
            "descricao": self.txt_desc.get("1.0", END).strip()
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
                messagebox.showwarning("Aviso", "Já existe um produto com este código!")
                return
                
            self.collection.insert_one(self.dados())
            self.limpar()
            self.lbl_resultado.config(text="✓ Produto salvo com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Produto salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar: {str(e)}")

    def atualizar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do produto!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Produto não encontrado!")
                return
                
            self.collection.update_one(
                {"codigo": codigo},
                {"$set": self.dados()}
            )
            
            self.lbl_resultado.config(text="✓ Produto atualizado com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            self.limpar()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

    def apagar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do produto!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})
            
            if not resultado:
                messagebox.showwarning("Aviso", "Produto não encontrado!")
                return
                
            resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o produto {codigo}?")
            
            if resposta:
                self.collection.delete_one({"codigo": codigo})
                self.limpar()
                self.lbl_resultado.config(text="✓ Produto excluído com sucesso!", fg="green")
                messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir: {str(e)}")

    def consultar(self):
        try:
            codigo = self.txt_codigo.get()
            
            if not codigo:
                messagebox.showwarning("Aviso", "Informe o código do produto!")
                return
                
            resultado = self.collection.find_one({"codigo": codigo})

            if resultado:
                self.limpar()

                self.txt_codigo.insert(0, resultado.get("codigo", ""))
                self.txt_nome.insert(0, resultado.get("nome", ""))
                self.combo_categoria.set(resultado.get("categoria", "Eletrônicos"))
                self.txt_quantidade.insert(0, str(resultado.get("quantidade", "")))
                self.txt_preco.insert(0, str(resultado.get("preco", "")))
                self.txt_fornecedor.insert(0, resultado.get("fornecedor", ""))
                self.txt_estoque_minimo.insert(0, str(resultado.get("estoque_minimo", "")))
                self.txt_localizacao.insert(0, resultado.get("localizacao", ""))
                self.txt_desc.insert('1.0', resultado.get("descricao", ""))
                
                self.lbl_resultado.config(text="✓ Produto encontrado!", fg="green")
            else:
                self.lbl_resultado.config(text="✗ Produto não encontrado!", fg="red")
                messagebox.showwarning("Aviso", "Produto não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar: {str(e)}")
    
    def sair(self):
        resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
        if resposta:
            self.tela.destroy()

# EXECUTAR
if __name__ == "__main__":
    ProdutosV()