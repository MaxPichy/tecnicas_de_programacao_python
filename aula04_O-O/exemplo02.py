class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método: calcular idade
    def calculaIdade(self):
        anoAtual = int(input('Digite o ano atual: '))
        return anoAtual - self.idade

# Instanciar objeto da classe Pessoa
p = Pessoa('Max', 20)
pe = Pessoa('Maomao', 17)
print(p.calculaIdade())
print(f'{pe.nome}, nasceu em {pe.calculaIdade()}')