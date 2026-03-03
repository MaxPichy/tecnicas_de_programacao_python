import os
os.system('cls')

tab = int(input('Tabuada do número: '))
de = int(input('De: '))
ate = int(input('Até: '))
while de < ate+1:
    result = de * tab;
    print(f'{tab} X {de} = {result}')
    de += 1;