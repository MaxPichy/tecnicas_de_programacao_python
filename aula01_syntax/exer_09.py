brancos = int(input('Digite o total de votos brancos: '))
nulos = int(input('Digite o total de votos nulos: '))
validos = int(input('Digite o total de votos válidos: '))

eleitores = int(brancos + nulos + validos)
perBrancos = float((brancos * 100) / eleitores)
perNulos = float((nulos * 100) / eleitores)
perValidos = float((validos * 100) / eleitores)

print(f'Total de Eleitores: {eleitores}; Percentuais: Válidos ({perValidos:.2f}%), Brancos ({perBrancos:.2f}%), Nulos ({perNulos:.2f}%).')