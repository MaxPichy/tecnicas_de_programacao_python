import math
raio = float(input('Digite o raio da lata em cm: '))
altura = float(input('Digite a altura da lata em cm: '))
volume = float(math.pi * (raio ** 2) * altura)

print(f'O volume da lata é de: {volume:.2f} cm*3.')