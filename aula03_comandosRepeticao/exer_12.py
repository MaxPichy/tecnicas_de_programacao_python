import os
os.system('cls')

lang = ["python","c#","VisualBasic","C++","Delphi","Cobol","Clipper","PHP","Java"]
buscar = input('Digite uma linguagem de programação: ')

i = 0
for lista in lang:
    if buscar == lista:
        print(f'{buscar} encontrado!')
        print(f'{buscar} foi encontrado na posição {i + 1}.')
    else:
        print(f'{buscar} não encontrado.')
        i += 1
