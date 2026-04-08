import tkinter as tk

class Media:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Calculadora de Soma')
        self.janela.geometry('600x400')
        self.janela.resizable(False, False)
        self.janela.configure(background='#AE798A')

        self.n1 = tk.StringVar()
        self.n2 = tk.StringVar()
        self.n3 = tk.StringVar()

        self.criar_widgets()
        
        self.janela.mainloop()
    
    def criar_widgets(self):
        self.label1 = tk.Label(self.janela, text='Digite o primeiro número:', fg='black', background="#AE798A")
        self.label1.pack(pady=5)
        
        self.entry1 = tk.Entry(self.janela, textvariable=self.n1, width=30)
        self.entry1.pack(pady=5)
        
        self.label2 = tk.Label(self.janela, text='Digite o segundo número:', fg='black', background='#AE798A')
        self.label2.pack(pady=5)
        
        self.entry2 = tk.Entry(self.janela, textvariable=self.n2, width=30)
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(self.janela, text='Digite o terceiro número:', fg='black', background='#AE798A')
        self.label3.pack(pady=5)
        
        self.entry3 = tk.Entry(self.janela, textvariable=self.n3, width=30)
        self.entry3.pack(pady=5)
        
        self.botao_calcular = tk.Button(
            self.janela, 
            text='Calcular Média', 
            command=self.calcular,
            bg="#EF0650", 
            font=('Arial', 10, 'bold'),
            fg='white'
        )
        self.botao_calcular.pack(pady=10)
        
        self.label_resultado = tk.Label(self.janela, text='', font='bold', background="#BF3B65")
        self.label_resultado.pack(pady=10)
    
    def calcular(self):
        n1 = float(self.n1.get())
        n2 = float(self.n2.get())
        n3 = float(self.n3.get())
        media = float((n1 + n2 + n3) / 3)

        if(media >= 7):
            self.label_resultado.config(text=f'Média: {media:.2f} \nResultado: Aprovado ')
        elif(media <= 3):
            self.label_resultado.config(text=f'Média: {media:.2f} \nResultado: Reprovado ')
        else:
            self.label_resultado.config(text=f'Média: {media:.2f} \nResultado: Exame ')
