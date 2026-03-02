import os 
os.system('cls')

menu = int(input('------ CÁLCULO DE GRANDEZAS ELÉTRICAS ------ \n 1 - Tensão (em Volt) \n 2 - Resistência (em Ohm) \n 3 - Corrente (em Ampére) \n --------------------------------------------- \n Digite a opção desejada: '))

if menu > 0 & menu < 4:
    match menu:
        case 1:
            r = float(input('Digite o valor da resistência (em ohm): '))
            i = float(input('Digite o valor da corrente (em ampéres): '))
            u = r * i
            print(f'A tensão é de: {u:.2f} volts.')

        case 2:
            u = float(input('Digite o valor da tensão (em volts)): '))
            i = float(input('Digite o valor da corrente (em ampéres): '))
            r = u / i
            print(f'A resistência é de: {r:.2f} ohm.')

        case 3:
            u = float(input('Digite o valor da tensão (em volts)): '))
            r = float(input('Digite o valor da resistência (em ohm): '))
            i = u / r
            print(f'A corrente é de: {i:.2f} ampéres.')
        
        case _:
            print('Opção Inválida.')