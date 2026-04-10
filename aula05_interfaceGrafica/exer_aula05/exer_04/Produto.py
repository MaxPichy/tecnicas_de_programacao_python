import tkinter as tk

class Produto:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Calculadora de Soma')
        self.janela.geometry('600x400')
        self.janela.resizable(False, False)
        self.janela.configure(background="#1D138F")

        self.nome = tk.StringVar()
        self.quantidade = tk.IntVar()
        self.valor = tk.DoubleVar()
        self.total = tk.DoubleVar()

        self.criar_widgets()
        
        self.janela.mainloop()

    def criar_widgets(self):
        self.label1 = tk.Label(self.janela, text='Digite o nome:', fg='white', background="#1D138F")
        self.label1.pack(pady=5)
        
        self.entry1 = tk.Entry(self.janela, textvariable=self.nome, width=30)
        self.entry1.pack(pady=5)
        
        self.label2 = tk.Label(self.janela, text='Digite a quantidade:', fg='white', background='#1D138F')
        self.label2.pack(pady=5)
        
        self.entry2 = tk.Entry(self.janela, textvariable=self.quantidade, width=30)
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(self.janela, text='Digite o valor:', fg='white', background='#1D138F')
        self.label3.pack(pady=5)
        
        self.entry3 = tk.Entry(self.janela, textvariable=self.valor, width=30)
        self.entry3.pack(pady=5)
        
        self.botao_calcular = tk.Button(
            self.janela, 
            text='Calcular Total', 
            command=self.calcular,
            bg="#B0ACD3", 
            font=('Arial', 10, 'bold'),
            fg='black'
        )
        self.botao_calcular.pack(pady=10)
        
        self.label_resultado = tk.Label(self.janela, text='', font='bold', background="#1F1A54", fg="white")
        self.label_resultado.pack(pady=10)
    
    def calcular(self):
        nome = self.nome.get()
        quantidade = self.quantidade.get()
        valor = self.valor.get()
        self.total = valor * quantidade
        total = self.total

        self.mostrarDadosProduto(nome, quantidade, valor, total)

    def mostrarDadosProduto(self, nome, quantidade, valor, total):
        self.label_resultado.config(text=f'Nome: {nome} \nQuantidade: {quantidade}\nValor: {valor:.2f}\n \n Total: {total:.2f}')