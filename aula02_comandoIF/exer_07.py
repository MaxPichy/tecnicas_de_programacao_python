rg = input('Digite o RG do funcionário: ')
nasc = int(input('Digite o ano de nascimento: '))
ing = int(input('Digite o ano de ingresso na empresa: '))
atual = int(input('Digite o ano atual: '))

idade = atual - nasc
trabalho = atual - ing

if idade >= 65:
    print('Requerer aposentadoria.')
elif trabalho >= 30:
    print('Requerer aposentadoria.')
elif idade >= 60 and trabalho >= 25:
    print('Requerer aposentadoria.')
else: 
    print('Não requerer aposentadoria.')