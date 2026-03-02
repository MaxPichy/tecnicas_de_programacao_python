import os
os.system('cls')

letra = input('Digite uma letra: ')

match letra.upper():
    case 'A' | 'I' | 'U' | 'E' | 'O':
        print('Você digitou uma vogal!')
    case _:
        print('Você digitou uma consoante.')