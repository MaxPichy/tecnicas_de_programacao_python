import tkinter as tk

class Clientes:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Cadastro de Clientes')
        self.janela.geometry('600x500')
        self.janela.resizable(False, False)
        self.janela.configure(background="#16555A")

        self.nome = tk.StringVar()
        self.email = tk.StringVar()
        self.telefone = tk.StringVar()
        self.endereco = tk.StringVar()
        
        self.criar_widgets()
        
        self.janela.mainloop()
    
    def criar_widgets(self):
        self.label1 = tk.Label(self.janela, text='Digite o nome:', fg='white', background='#16555A')
        self.label1.pack(pady=5)
        
        self.entry1 = tk.Entry(self.janela, textvariable=self.nome, width=30)
        self.entry1.pack(pady=5)
        
        self.label2 = tk.Label(self.janela, text='Digite o email:', fg='white', background='#16555A')
        self.label2.pack(pady=5)
        
        self.entry2 = tk.Entry(self.janela, textvariable=self.email, width=30)
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(self.janela, text='Digite o telefone:', fg='white', background='#16555A')
        self.label3.pack(pady=5)
        
        self.entry3 = tk.Entry(self.janela, textvariable=self.telefone, width=30)
        self.entry3.pack(pady=5)

        self.label4 = tk.Label(self.janela, text='Digite o endereço:', fg='white', background='#16555A')
        self.label4.pack(pady=5)
        
        self.entry4 = tk.Entry(self.janela, textvariable=self.endereco, width=30)
        self.entry4.pack(pady=5)
        
        self.botao_cadastrar = tk.Button(
            self.janela, 
            text='Cadastrar', 
            command=self.cadastrarCliente,
            bg="#BEECEF", 
            font=('Arial', 10, 'bold'),
            fg='black'
        )
        self.botao_cadastrar.pack(pady=10)
        
        self.label_resultado = tk.Label(self.janela, text='', font='bold', background="#88EAF1")
        self.label_resultado.pack(pady=10)
    
    def cadastrarCliente(self):
        nome = self.nome.get()
        email = self.email.get()
        telefone = self.telefone.get()
        endereco = self.endereco.get()

        self.mostrarDados(nome, email, telefone, endereco)
    
    def mostrarDados(self, nome, email, telefone, endereco):
        self.label_resultado.config(text=f'Nome: {nome}\n Email: {email}\n Telefone: {telefone}\n Endereço: {endereco}')