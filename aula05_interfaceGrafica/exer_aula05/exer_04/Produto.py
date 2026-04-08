import tkinter as tk

class Produto:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Calculadora de Soma')
        self.janela.geometry('600x400')
        self.janela.resizable(False, False)
        self.janela.configure(background='#AE798A')

        self.nome = tk.StringVar()
        self.quantidade = tk.StringVar()
        self.valor = tk.StringVar()
        self.total = 0

        self.criar_widgets()
        
        self.janela.mainloop()

    def criar_widgets(self):
        self.label1 = tk.Label(self.janela, text='Digite o nome:', fg='black', background="#AE798A")
        self.label1.pack(pady=5)
        
        self.entry1 = tk.Entry(self.janela, textvariable=self.nome, width=30)
        self.entry1.pack(pady=5)
        
        self.label2 = tk.Label(self.janela, text='Digite a quantidade:', fg='black', background='#AE798A')
        self.label2.pack(pady=5)
        
        self.entry2 = tk.Entry(self.janela, textvariable=self.quantidade, width=30)
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(self.janela, text='Digite o valor:', fg='black', background='#AE798A')
        self.label3.pack(pady=5)
        
        self.entry3 = tk.Entry(self.janela, textvariable=self.valor, width=30)
        self.entry3.pack(pady=5)
        
        self.botao_calcular = tk.Button(
            self.janela, 
            text='Calcular Total', 
            command=self.calcular,
            bg="#EF0650", 
            font=('Arial', 10, 'bold'),
            fg='white'
        )
        self.botao_calcular.pack(pady=10)
        
        self.label_resultado = tk.Label(self.janela, text='', font='bold', background="#BF3B65")
        self.label_resultado.pack(pady=10)
    
    def calcular(self):
        quantidade = float(self.quantidade.get())
        valor = float(self.valor.get())
        self.total = valor * quantidade
    
    def mostrarDadosProduto(self):
        nome = self.nome.get()
        quantidade = float(self.quantidade.get())
        valor = float(self.valor.get())
        total = self.total.get()

        self.label_resultado.config(text=f'Nome: {nome} \nQuantidade: {quantidade}\nValor: {valor:.2f}\n \n Total: {total:.2f}')