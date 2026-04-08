import tkinter as tk

class Soma:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Calculadora de Soma')
        self.janela.geometry('300x250')
        self.janela.resizable(False, False)
        self.janela.configure(background='#54118C')

        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        
        self.criar_widgets()
        
        self.janela.mainloop()
    
    def criar_widgets(self):
        self.label1 = tk.Label(self.janela, text='Digite o primeiro número:', fg='white', background='#54118C')
        self.label1.pack(pady=5)
        
        self.entry1 = tk.Entry(self.janela, textvariable=self.num1, width=30)
        self.entry1.pack(pady=5)
        
        self.label2 = tk.Label(self.janela, text='Digite o segundo número:', fg='white', background='#54118C')
        self.label2.pack(pady=5)
        
        self.entry2 = tk.Entry(self.janela, textvariable=self.num2, width=30)
        self.entry2.pack(pady=5)
        
        self.botao_calcular = tk.Button(
            self.janela, 
            text='Calcular Soma', 
            command=self.calcular,
            bg='#270445', 
            font=('Arial', 10, 'bold'),
            fg='white'
        )
        self.botao_calcular.pack(pady=10)
        
        self.label_resultado = tk.Label(self.janela, text='', font='bold', background='#9269B4')
        self.label_resultado.pack(pady=10)
    
    def calcular(self):
        n1 = int(self.num1.get())
        n2 = int(self.num2.get())
        soma = n1 + n2

        self.label_resultado.config(text=f'Soma: {soma}')