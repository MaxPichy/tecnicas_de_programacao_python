a = float(input('Digite a altura em m: '))
s = input('Digite o sexo como M (masculino) ou F (feminino): ')

if s == 'M':
    peso = (72.7 * a) - 58
    print(f'Altura: {a}; Sexo: {s}; Peso Ideal: {peso}')
elif s == 'F':
    peso = (62.1 * a) - 44.7
    print(f'Altura: {a}; Sexo: {s}; Peso Ideal: {peso:.2f}')
else:
    print('Dados fornecidos incorretamente.')