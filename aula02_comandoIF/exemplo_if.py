#Exemplo Estrutura Condicional IF - Média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

#Comando IF
if media > 6.0:
    print(f"Aluno Aprovado! A média é de {media:.2f}.")
elif media > 5 and media < 6:
    print(f"Aluno em Exame! A média é de {media:.2f}.")
else:
    print(f"Aluno Reprovado! A média é de {media:.2f}.")