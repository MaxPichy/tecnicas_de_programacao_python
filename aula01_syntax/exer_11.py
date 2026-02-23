nome = str(input('Digite o nome do produto: '))
quantidade = int(input('Digite a quantidade comprada: '))
preco = float(input('Digite o preço do produto: '))
precoTotal = float(quantidade * preco)

print(f'O total a ser pago por {quantidade} {nome} é de R${precoTotal:.2f}.')