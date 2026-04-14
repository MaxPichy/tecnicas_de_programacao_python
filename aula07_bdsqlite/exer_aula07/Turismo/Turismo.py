from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import sys
import sqlite3


class Turismo:

    def __init__(self):
        self.tela = Tk()
      
        self.configurar_tela()
        self.criar_componentes()
        self.criar_banco()

    # ---------------------------
    def configurar_tela(self):
        
        self.tela.title("Controle de Locais Turísticos")
        self.tela.config(background="#88cf9f")

        self.largura = 1000
        self.altura = 700

        self.var = StringVar()
        self.var.set("s")

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))
        
    # CRIAR BANCO DE DADOS SQLITE
    def criar_banco(self):
        self.conn = sqlite3.connect("turismo.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS turismo (
            codigo INTEGER PRIMARY KEY,
            nome TEXT,
            entrada REAL,
            cidade TEXT,
            estado TEXT,
            guia TEXT
        )
        """)
        self.conn.commit()    
        
    # PARA SALVAR OS DADOS NO BD SQLITE
    def salvar(self):
        try:
            self.cursor.execute("""
            INSERT INTO turismo (
                codigo, nome, entrada, cidade, estado, guia
            ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.txt_codigo.get(),
                self.txt_nome.get(),
                self.txt_entrada.get(),
                self.txt_cidade.get(),
                self.cmb_estado.get(),
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
        Label(self.tela, text="Entrada:").place(x=180, y=130)
        Label(self.tela, text="Cidade:").place(x=180, y=170)
        Label(self.tela, text="Estado:").place(x=180, y=210)
        Label(self.tela, text="Guia:").place(x=180, y=250)

        # Caixas de Texto
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_codigo.place(x=250, y=50)
        
        self.txt_nome = Entry(self.tela, width=40)
        self.txt_nome.place(x=250, y=90)
        
        self.txt_entrada = Entry(self.tela, width=20)
        self.txt_entrada.place(x=250, y=130)
        
        self.txt_cidade = Entry(self.tela, width=20)
        self.txt_cidade.place(x=250, y=170)                                                     

        # Combobox (Marca)
        self.cmb_estado = ttk.Combobox(self.tela, width=17)
        self.cmb_estado['values'] = (
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", 
            "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", 
            "RS", "RO", "RR", "SC", "SP", "SE", "TO"
        )
        self.cmb_estado.current(1)
        self.cmb_estado.place(x=250, y=210)

        # Radio buttons
        Radiobutton(self.tela, text="Sim", variable=self.var, value="s").place(x=250, y=250)
        Radiobutton(self.tela, text="Não", variable=self.var, value="n").place(x=370, y=250)

        # Botões com ícones
        self.foto_salvar = PhotoImage(file="iconesturismo/cadastrar.png")
        self.foto_excluir = PhotoImage(file="iconesturismo/excluir.png")
        self.foto_alterar = PhotoImage(file="iconesturismo/alterar.png")
        self.foto_consultar = PhotoImage(file="iconesturismo/consultar.png")
        self.foto_sair = PhotoImage(file="iconesturismo/sair.png")
        self.foto_escolher = PhotoImage(file="iconesturismo/escimagem.png")

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
        self.btn_escolher = Button(self.tela, text="Escolher Imagem", image=self.foto_escolher, compound=TOP, command=self.escolher_imagem)
        self.btn_escolher.place(x=20, y=200)

        # TABELA PARA MOSTRAR DADOS SQLITE
        self.tree = ttk.Treeview(self.tela, columns=("cod", "nome", "entrada", "cidade", "estado", "guia"), show="headings")

        self.tree.heading("cod", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("entrada", text="Entrada")
        self.tree.heading("cidade", text="Cidade")
        self.tree.heading("estado", text="Estado")
        self.tree.heading("guia", text="Guia")

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

        self.txt_entrada.delete(0, END)
        self.txt_entrada.insert(0, dados[2])
        
        self.txt_cidade.delete(0, END)
        self.txt_cidade.insert(0, dados[3])

        self.cmb_estado.set(dados[4])
        self.var.set(dados[5])
        
    # ATUALIZAR DADOS SQLITE
    def atualizar(self):
        self.cursor.execute("""
        UPDATE turismo SET
            nome=?,
            entrada=?,
            cidade=?,
            estado=?,
            guia=?
        WHERE codigo=?
        """, (
            self.txt_nome.get(),
            self.txt_entrada.get(),
            self.txt_cidade.get(),
            self.cmb_estado.get(),
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

        self.cursor.execute("SELECT codigo, nome, entrada, cidade, estado, guia FROM turismo")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)
    
    # EXCLUIR DADOS BANCO DE DADOS
    def excluir(self):
        self.cursor.execute("DELETE FROM turismo WHERE codigo=?", (self.txt_codigo.get(),))
        self.conn.commit()
        self.consultar_dados()
        Label(self.tela, text="Dados excluídos com sucesso!", fg="green").place(x=20, y=360)

    def executar(self):
        self.tela.mainloop()


# Para executar
if __name__ == "__main__":
    app = Turismo()
    app.executar()