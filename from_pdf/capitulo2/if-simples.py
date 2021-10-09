# VARIAVEIS
nome = input("Digite o nome: ").capitalize()
idade = int(input("Digite sua idade: "))
prioridade = "NÃO"

# CONDIÇÃO
if idade >= 65:
    prioridade = "SIM"

# IMPRESSÃO
print(f"\nO paciente {nome} possui atendimento priritário? {prioridade}!\n")