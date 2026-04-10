import tkinter as tk

class Contatos:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Cadastro de Contatos')
        self.janela.geometry('600x500')
        self.janela.resizable(False, False)
        self.janela.configure(background="#3B9A7F")

        self.nome = tk.StringVar()
        self.telefone = tk.StringVar()
        self.endereco = tk.StringVar()
        self.cidade = tk.StringVar()

        self.criar_widgets()
        
        self.janela.mainloop()

    def criar_widgets(self):
        self.label1 = tk.Label(self.janela, text='Digite o nome:', fg='black', background="#3B9A7F")
        self.label1.pack(pady=5)
        
        self.entry1 = tk.Entry(self.janela, textvariable=self.nome, width=30)
        self.entry1.pack(pady=5)
        
        self.label2 = tk.Label(self.janela, text='Digite a telefone:', fg='black', background='#3B9A7F')
        self.label2.pack(pady=5)
        
        self.entry2 = tk.Entry(self.janela, textvariable=self.telefone, width=30)
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(self.janela, text='Digite o endereço:', fg='black', background='#3B9A7F')
        self.label3.pack(pady=5)
        
        self.entry3 = tk.Entry(self.janela, textvariable=self.endereco, width=30)
        self.entry3.pack(pady=5)

        self.label4 = tk.Label(self.janela, text='Digite o cidade:', fg='black', background='#3B9A7F')
        self.label4.pack(pady=5)
        
        self.entry4 = tk.Entry(self.janela, textvariable=self.cidade, width=30)
        self.entry4.pack(pady=5)
        
        self.botao_cadastrar = tk.Button(
            self.janela, 
            text='Cadastrar Contato', 
            command=self.cadastrarDados,
            bg="#077F5D", 
            font=('Arial', 10, 'bold'),
            fg='black'
        )
        self.botao_cadastrar.pack(pady=10)
        
        self.label_resultado = tk.Label(self.janela, text='', font='bold', background="#267861", fg="white")
        self.label_resultado.pack(pady=10)

    def cadastrarDados(self):
        nome = self.nome.get()
        telefone = self.telefone.get() 
        endereco = self.endereco.get()
        cidade = self.cidade.get()

        self.mostrarDados(nome, telefone, endereco, cidade)

    def mostrarDados(self, nome, telefone, endereco, cidade):
        self.label_resultado.config(text=f'Nome: {nome} \nTelefone: {telefone}\nEndereço: {endereco} \nCidade: {cidade}')