num = float(input('Digite o número: '))
exp = float(input('Digite o expoente: '))

#Potencia utilizando o operador
pot = num ** exp
#Potencia utilizando a funcao math
potencia = pow(num, exp)

print(f'A potência de {num} pelo expoente {exp} é (**) {pot}, ou (power) {potencia}')