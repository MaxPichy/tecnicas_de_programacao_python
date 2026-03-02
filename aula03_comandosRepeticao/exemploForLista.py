import os
os.system('cls')

# Exemplo for utilizando lista de valores pre-definida

frutas = ['banana', 'pitaya', 'melão', 'abacaxi', 'uva']
for lista in frutas:
    print(lista)

buscar = 'melão'
frutas = ['banana', 'pitaya', 'melão', 'abacaxi', 'uva']
for lista in frutas:
    if lista == buscar:
        print(f'Fruta encontrada: {buscar}.')
        break
    else:
        print(f'Fruta não encontrada... {buscar}')