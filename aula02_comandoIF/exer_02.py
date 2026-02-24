nome1 = input('Digite o nome da pessoa 1: ')
peso1 = float(input('Digite o peso da pessoa 1 em kg: '))

nome2= input('Digite o nome da pessoa 2: ')
peso2 = float(input('Digite o peso da pessoa 2 em kg: '))

if peso1 > peso2:
    print(f'A pessoa mais pesada é: {nome1}, com {peso1} kg.')
elif peso2 > peso1:
    print(f'A pessoa mais pesada é: {nome2}, com {peso2} kg.')
else:
    print('As pessoas possuem o mesmo peso corporal.')