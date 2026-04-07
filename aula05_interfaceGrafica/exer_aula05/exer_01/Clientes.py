from tkinter import * 

class Clientes:
    def __init__(self):
        # Atributos
        self.__nome = ''
        self.__email = ''
        self.__telefone = ''
        self.__endereco = '' 

        # Configs da interface
        self.tela = Tk()  
        self.config_tela()
        self.componentes()

    # Getters e Setters
    @property
    def nome(self): 
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    def config_tela(self):
        self.tela.title("Cadastro - Clientes")
        self.tela.configure(background="#6AD2B1")

        wid_screen = self.tela.winfo_screenwidth()
        hei_screen = self.tela.winfo_screenheight()

        width = 800
        height = 500 

        posx = wid_screen / 2 - width / 2
        posy = hei_screen / 2 - height / 2

        self.tela.geometry('%dx%d+%d+%d' % (width, height, posx, posy))

    def componentes(self):
        # Frame principal
        main_frame = Frame(self.tela, bg="#6AD2B1")
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.frame_cadastro = Frame(main_frame, bg="#1D936A", padx=20, pady=10)
        self.frame_cadastro.pack(fill='x', pady=(0, 10))  # CORRIGIDO: sem expand
        
        self.frame_exibicao = Frame(main_frame, bg="#1D936A", padx=20, pady=10)
        self.frame_exibicao.pack(fill='both', expand=True)  # CORRIGIDO: com expand
        
        # Cadastro
        self.titulo_cadastro = Label(self.frame_cadastro, text="Cadastro - Clientes")
        self.titulo_cadastro.grid(row=0, column=0, columnspan=2, pady=5)

        Label(self.frame_cadastro, text="Nome:").grid(row=1, column=0, pady=5, sticky='e')
        self.nome_entry = Entry(self.frame_cadastro, width=30)
        self.nome_entry.grid(row=1, column=1, pady=5, padx=5)

        Label(self.frame_cadastro, text="Email:").grid(row=2, column=0, pady=5, sticky='e')
        self.email_entry = Entry(self.frame_cadastro, width=30)
        self.email_entry.grid(row=2, column=1, pady=5, padx=5)

        Label(self.frame_cadastro, text="Telefone:").grid(row=3, column=0, pady=5, sticky='e')
        self.telefone_entry = Entry(self.frame_cadastro, width=30)
        self.telefone_entry.grid(row=3, column=1, pady=5, padx=5)

        Label(self.frame_cadastro, text="Endereço:").grid(row=4, column=0, pady=5, sticky='e')
        self.endereco_entry = Entry(self.frame_cadastro, width=30)
        self.endereco_entry.grid(row=4, column=1, pady=5, padx=5)

        self.btn = Button(self.frame_cadastro, text="Cadastrar", command=self.cadastrar_cliente, bg="#B3EFD9", fg="black")
        self.btn.grid(row=5, column=0, columnspan=2, pady=10)

        self.titulo_exibicao = Label(self.frame_exibicao, text="Dados do Cliente")
        self.titulo_exibicao.pack(pady=5)
        
        # Frame para os dados
        dados_frame = Frame(self.frame_exibicao, bg="#0F6B4A", padx=10, pady=10)
        dados_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Labels com os dados (inicialmente vazios)
        self.label_nome = Label(dados_frame, text="Nome:", bg="#0F6B4A", fg="white")
        self.label_nome.pack(anchor='w', pady=5)
        
        self.label_email = Label(dados_frame, text="Email:", bg="#0F6B4A", fg="white")
        self.label_email.pack(anchor='w', pady=5)
        
        self.label_telefone = Label(dados_frame, text="Telefone:", bg="#0F6B4A", fg="white")
        self.label_telefone.pack(anchor='w', pady=5)
        
        self.label_endereco = Label(dados_frame, text="Endereço:", bg="#0F6B4A", fg="white")
        self.label_endereco.pack(anchor='w', pady=5)

    def cadastrar_cliente(self):
        nome_valor = self.nome_entry.get()
        email_valor = self.email_entry.get()
        telefone_valor = self.telefone_entry.get()
        endereco_valor = self.endereco_entry.get()

        self.nome = nome_valor
        self.email = email_valor
        self.telefone = telefone_valor
        self.endereco = endereco_valor
        
        self.label_nome.config(text=f"Nome: {nome_valor}")
        self.label_email.config(text=f"Email: {email_valor}")
        self.label_telefone.config(text=f"Telefone: {telefone_valor}")
        self.label_endereco.config(text=f"Endereço: {endereco_valor}")

    def rodar(self):
        self.tela.mainloop()

if __name__ == "__main__":
    app = Clientes()
    app.rodar()