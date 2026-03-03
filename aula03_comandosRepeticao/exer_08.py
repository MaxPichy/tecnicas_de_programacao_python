import os
os.system('cls')

num = []
for i in range(1, 11):
    n = float(input('Digite um número: '))
    num.append(n)

for i in num:
    if(i % 2 == 0):
        print(f'{i:.2f} = par.')
    else:
        print(f'{i:.2f} = ímpar.')