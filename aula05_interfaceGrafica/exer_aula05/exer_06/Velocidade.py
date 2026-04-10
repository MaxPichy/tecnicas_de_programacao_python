import tkinter as tk

class Velocidade:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Calculadora de Velocidade')
        self.janela.geometry('600x500')
        self.janela.resizable(False, False)
        self.janela.configure(background="#E38C91")

        self.nome = tk.StringVar()
        self.distancia = tk.DoubleVar()
        self.tempo = tk.DoubleVar()
        self.velocidade = tk.DoubleVar()
        
        self.criar_widgets()
        
        self.janela.mainloop()

    def criar_widgets(self):
        self.label1 = tk.Label(self.janela, text='Digite o nome do carro:', fg='black', background="#E38C91")
        self.label1.pack(pady=5)
        
        self.entry1 = tk.Entry(self.janela, textvariable=self.nome, width=30)
        self.entry1.pack(pady=5)
        
        self.label2 = tk.Label(self.janela, text='Digite a distância em km:', fg='black', background='#E38C91')
        self.label2.pack(pady=5)
        
        self.entry2 = tk.Entry(self.janela, textvariable=self.distancia, width=30)
        self.entry2.pack(pady=5)

        self.label3 = tk.Label(self.janela, text='Digite o tempo em minutos:', fg='black', background='#E38C91')
        self.label3.pack(pady=5)
        
        self.entry3 = tk.Entry(self.janela, textvariable=self.tempo, width=30)
        self.entry3.pack(pady=5)
        
        self.botao_calcular = tk.Button(
            self.janela, 
            text='Calcular Velocidade', 
            command=self.calcularVelocidade,
            bg="#82151A", 
            font=('Arial', 10, 'bold'),
            fg='white'
        )
        self.botao_calcular.pack(pady=10)
        
        self.label_resultado = tk.Label(self.janela, text='', font='bold', background="#F05C64", fg="white")
        self.label_resultado.pack(pady=10)
        
    def calcularVelocidade(self):
        nome = self.nome.get()
        distancia = self.distancia.get()
        tempo = self.tempo.get()
        velocidade = (distancia * 1000) / (tempo * 60)
        self.velocidade = velocidade

        self.mostrarResultado(nome, distancia, tempo, velocidade)
        
    def mostrarResultado(self, nome, distancia, tempo, velocidade):
        self.label_resultado.config(text=f'Carro: {nome} \nDistância: {(distancia * 1000):.2f} m\nTempo: {(tempo * 60):.2f} s \n \nVelocidade: {velocidade:.2f} m/s')
