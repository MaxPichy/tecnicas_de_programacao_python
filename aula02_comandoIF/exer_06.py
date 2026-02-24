num1 = float(input('Digite o primeiro número positivo: '))
num2 = float(input('Digite o primeiro número positivo: '))

if num1 > 0 and num2 > 0: 
    menu = int(input('1 - Média ponderada com pesos 2 e 3, respectivamente: \n2 - Quadrado da soma dos dois números \n3 - Cubo do menor número: '))

    if menu == 1:
        media = (num1 * 2 + num2 * 3) / 5
        print(f'Resultado: {media}.')

    elif menu == 2:
        qs = (num1 + num2) ** 2
        print(f'Resultado: {qs}.')

    elif menu == 3:
        if num1 > num2:
            c = num2 ** 3
            print(f'Resultado: {c}.')
        elif num2 > num1:
            c = num1 ** 3
            print(f'Resultado: {c}.')
        else:
            print('Os números são iguais.')
    else: 
        print('Opção inválida fornecida.')
    
else: 
    print('Dado inválido fornecido.')