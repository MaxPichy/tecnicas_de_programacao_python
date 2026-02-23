salario = float(input('Digite o salário atual: '))
aumento = float(input('Digite o percentual de aumento do salário: '))
salarioCorrigido = float((salario * aumento) / 100 + salario)

print(f'O valor do salário corrigido é de: R$ {salarioCorrigido:.2f}.')