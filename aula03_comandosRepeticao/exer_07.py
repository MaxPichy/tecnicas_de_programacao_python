import os
os.system('cls')

nomes = []
for i in range(1, 8):
    nome = input(f'Digite o {i} nome: ')
    nomes.append(nome)

c = 1;
for i in nomes:
    print(f'O {c} nome armazenado é: {i}')
    c+=1
