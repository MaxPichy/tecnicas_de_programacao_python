import os 
os.system('cls')

pol = int(input('Digite o índice de poluição da empresa: '))
if pol >= 0:
    match pol:
        case 0 | 1 | 2:
            print('Ação: Não necessária a princípio. O índice é aceitável.')

        case 3 | 4 | 5:
            print('Ação: Suspender Atividades. Grupo I.')

        case 6 | 7:
            print('Ação: Suspender Atividades. Grupo II.')

        case _:
            print('Ação: SUSPENDER TODAS AS ATIVIDADES. Todos os grupos.')