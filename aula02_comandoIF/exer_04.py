num = int(input('Digite um número inteiro positivo: '))

if num < 0:
    print('Dado incorreto fornecido.')
else: 
    if num % 2 == 0:
        q = num ** 2
        print(f'O número {num} é par, e o quadrado do número é: {q}')
    elif num % 2 != 0:
        c = num ** 3
        print(f'O número {num} é ímpar, e o cubo do número é: {c}.')