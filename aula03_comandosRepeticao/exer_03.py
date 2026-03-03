import os
os.system('cls')

tab = int(input('Tabuada do número: '))
counter = 1
while counter < 11:
    result = counter * tab;
    print(f'{tab} X {counter} = {result}')
    counter += 1;