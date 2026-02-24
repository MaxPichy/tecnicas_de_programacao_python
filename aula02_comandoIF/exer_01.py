n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    div = n1 / n2
    print(f'A divisão resulta em {div:.2f}.')
elif n2 > n1:
    div = n2 / n1
    print(f'A divisão resulta em {div:.2f}.')
else:
    print('Os números digitados são iguais.')