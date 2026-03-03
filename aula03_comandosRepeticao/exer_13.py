import os
os.system('cls')

n = []
s = []

i = 1
while i < 16:
    nome = input(f'Digite o nome do/a funcionário/a {i}: ')
    sexo = input(f'Digite o sexo do/a funcionário/a {i} (F/M): ')
    n.append(nome)
    s.append(sexo)
    i += 1

i = 0
while i < len(s):
    if(s[i].upper() == 'F'):
        print(f'Nome: {n[i]} \n Não precisa realizar o exame.')
    elif(s[i].upper() == 'M'):
        print(f'Nome: {n[i]} \n Precisa realizar o exame.')
    else: 
        print('Sexo digitado incorretamente.')
    i += 1