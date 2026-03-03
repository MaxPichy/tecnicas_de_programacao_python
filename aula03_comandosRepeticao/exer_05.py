import os
os.system('cls')

nomes = ['Maria', 'João', 'Paulo', 'Magali']
buscar = input('Digite um nome: ')

for lista in nomes:
    if buscar == lista:
        print(f'Nome Encontrado: {buscar}')
    else:
        print('Nome não encontrado.')