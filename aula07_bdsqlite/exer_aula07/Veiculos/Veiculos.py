from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import sys
import sqlite3


class Veiculos:

    def __init__(self):
        self.tela = Tk()
      
        self.configurar_tela()
        self.criar_componentes()
        self.criar_banco()

    # ---------------------------
    def configurar_tela(self):
        
        self.tela.title("Cadastro de Veículos")
        self.tela.config(background="#cdd390")

        self.largura = 1000
        self.altura = 700

        self.var = StringVar()
        self.var.set("utilitario")

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        
    # CRIAR BANCO DE DADOS SQLITE
    def criar_banco(self):
        self.conn = sqlite3.connect("veiculos.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            codigo INTEGER PRIMARY KEY,
            nome TEXT,
            placa TEXT,
            modelo TEXT,
            marca TEXT,
            utilitario TEXT
        )
        """)
        self.conn.commit()    
        
    # PARA SALVAR OS DADOS NO BD SQLITE
    def salvar(self):
        try:
            self.cursor.execute("""
            INSERT INTO veiculos (
                codigo, nome, placa, modelo, marca, utilitario
            ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.txt_codigo.get(),
                self.txt_nome.get(),
                self.txt_placa.get(),
                self.txt_modelo.get(),
                self.cmb_marca.get(),
                self.var.get(),
            ))

            self.conn.commit()
            self.consultar_dados()  
            Label(self.tela, text="Dados salvos com sucesso!", fg="green").place(x=20, y=320)

        except Exception as e:
            Label(self.tela, text=f"Erro: {e}", fg="red").place(x=20, y=320)

    # FUNÇÃO SAIR DA APLICAÇÃO
    def sair(self):
        self.conn.close()
        self.tela.destroy()
        sys.exit()
        
    # ---------------------------
    def escolher_imagem(self):
        caminho = filedialog.askopenfilename(
            title="Escolha uma imagem",
            filetypes=(("Imagens", "*.jpg;*.jpeg;*.png"), ("Todos", "*.*"))
        )

        if caminho:
            imagem = Image.open(caminho)
            largura, altura = imagem.size

            if largura > 150:
                proporcao = largura / 150
                nova_altura = int(altura / proporcao)
                imagem = imagem.resize((110, nova_altura))

            imagem_tk = ImageTk.PhotoImage(imagem)

            self.lbl_imagem = Label(self.tela, image=imagem_tk, width=95, height=140, bg="gray")
            self.lbl_imagem.image = imagem_tk
            self.lbl_imagem.place(x=20, y=50)

    # ---------------------------
    def criar_componentes(self):

        # Labels
        Label(self.tela, text="Código:").place(x=180, y=50)
        Label(self.tela, text="Nome:").place(x=180, y=90)
        Label(self.tela, text="Placa:").place(x=180, y=130)
        Label(self.tela, text="Modelo:").place(x=180, y=170)
        Label(self.tela, text="Marca:").place(x=180, y=210)
        Label(self.tela, text="Utilitário:").place(x=180, y=250)

        # Caixas de Texto
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_codigo.place(x=250, y=50)
        
        self.txt_nome = Entry(self.tela, width=40)
        self.txt_nome.place(x=250, y=90)
        
        self.txt_placa = Entry(self.tela, width=20)
        self.txt_placa.place(x=250, y=130)
        
        self.txt_modelo = Entry(self.tela, width=20)
        self.txt_modelo.place(x=250, y=170)                                                     

        # Combobox (Marca)
        self.cmb_marca = ttk.Combobox(self.tela, width=17)
        self.cmb_marca['values'] = ("Fiat", "Chevrolet", "Suzuki", "Wolkswagen", "Renault", "Ford")
        self.cmb_marca.current(1)
        self.cmb_marca.place(x=250, y=210)

        # Radio buttons (Utilitário)
        Radiobutton(self.tela, text="Utilitário", variable=self.var, value="utilitario").place(x=250, y=250)
        Radiobutton(self.tela, text="Não utilitário", variable=self.var, value="nao_utilitario").place(x=370, y=250)

        # Botões com ícones
        self.foto_salvar = PhotoImage(file="iconcarro/cadastrar.png")
        self.foto_excluir = PhotoImage(file="iconcarro/excluir.png")
        self.foto_alterar = PhotoImage(file="iconcarro/alterar.png")
        self.foto_consultar = PhotoImage(file="iconcarro/consultar.png")
        self.foto_sair = PhotoImage(file="iconcarro/sair.png")

        self.btn_salvar = Button(self.tela, text="Salvar", image=self.foto_salvar, compound=TOP, command=self.salvar)
        self.btn_salvar.place(x=180, y=300)

        self.btn_excluir = Button(self.tela, text="Excluir", image=self.foto_excluir, compound=TOP, command=self.excluir)
        self.btn_excluir.place(x=260, y=300)
        
        self.btn_alterar = Button(self.tela, text="Alterar", image=self.foto_alterar, compound=TOP, command=self.atualizar)
        self.btn_alterar.place(x=340, y=300)

        self.btn_consultar = Button(self.tela, text="Consultar", image=self.foto_consultar, compound=TOP, command=self.consultar_dados)        
        self.btn_consultar.place(x=420, y=300)

        self.btn_sair = Button(self.tela, text="Sair", image=self.foto_sair, compound=RIGHT, command=self.sair)  
        self.btn_sair.place(x=700, y=300)

        # Botão escolher imagem
        Button(self.tela, text="Escolher imagem", command=self.escolher_imagem).place(x=20, y=200)

        # TABELA PARA MOSTRAR DADOS SQLITE
        self.tree = ttk.Treeview(self.tela, columns=("cod", "nome", "placa", "modelo", "marca", "utilitario"), show="headings")

        self.tree.heading("cod", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("placa", text="Placa")
        self.tree.heading("modelo", text="Modelo")
        self.tree.heading("marca", text="Marca")
        self.tree.heading("utilitario", text="Utilitário")

        self.tree.place(x=20, y=380, width=960, height=250)

        self.tree.bind("<ButtonRelease-1>", self.selecionar_item)
        
    # SELECIONAR ITEMS DA TABELA BANCO DE DADOS
    def selecionar_item(self, event):
        item = self.tree.selection()[0]
        dados = self.tree.item(item, "values")

        self.txt_codigo.delete(0, END)
        self.txt_codigo.insert(0, dados[0])

        self.txt_nome.delete(0, END)
        self.txt_nome.insert(0, dados[1])

        self.txt_placa.delete(0, END)
        self.txt_placa.insert(0, dados[2])
        
        self.txt_modelo.delete(0, END)
        self.txt_modelo.insert(0, dados[3])

        self.cmb_marca.set(dados[4])
        self.var.set(dados[5])
        
    # ATUALIZAR DADOS SQLITE
    def atualizar(self):
        self.cursor.execute("""
        UPDATE veiculos SET
            nome=?,
            placa=?,
            modelo=?,
            marca=?,
            utilitario=?
        WHERE codigo=?
        """, (
            self.txt_nome.get(),
            self.txt_placa.get(),
            self.txt_modelo.get(),
            self.cmb_marca.get(),
            self.var.get(),
            self.txt_codigo.get()
        ))

        self.conn.commit()
        self.consultar_dados()
        Label(self.tela, text="Dados atualizados com sucesso!", fg="green").place(x=20, y=360)
        
    # CONSULTAR DADOS SQLITE
    def consultar_dados(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.cursor.execute("SELECT codigo, nome, placa, modelo, marca, utilitario FROM veiculos")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)
    
    # EXCLUIR DADOS BANCO DE DADOS
    def excluir(self):
        self.cursor.execute("DELETE FROM veiculos WHERE codigo=?", (self.txt_codigo.get(),))
        self.conn.commit()
        self.consultar_dados()
        Label(self.tela, text="Dados excluídos com sucesso!", fg="green").place(x=20, y=360)

    def executar(self):
        self.tela.mainloop()


# Para executar
if __name__ == "__main__":
    app = Veiculos()
    app.executar()