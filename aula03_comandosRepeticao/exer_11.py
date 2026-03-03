import os
os.system('cls')

lang = ['python', 'c#', 'Visual Basic', 'C++', 'Delphi', 'Cobol']

for i in lang:
    if(len(i) > 3):
        print(f'O nome da linguagem possui mais de 3 caracteres: {i}')

for i in lang:
    print(f'{i} contém {len(i)} caracteres.')
