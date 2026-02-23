#Executa cls automáticamente
import os 
os.system('cls')

print("$$$ Programa de Empréstimos $$$ \n  Responda (0 - Não 1; - Sim)")

neg = int(input("Possui nome negativo? "))
if neg == 1:
    print("Você não pode realizar empréstimos.")
else:
    carteira = int(input("Você possui carteira assinada? "))
    if carteira == 0:
        print("Não pode realizar empréstimos.")
    else:
        casa = int(input("Possui casa própria? "))
        if casa == 0:
            print("Não pode realizar empréstimos.")
