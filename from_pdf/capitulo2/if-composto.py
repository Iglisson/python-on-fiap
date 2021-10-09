# VARIAVEIS
nome = input("Digite o nome: ").capitalize()
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeta de doença infecto-contagiosa? ").upper()

# ESTRUTURA DE DECISÃO COMPOSTA SEM ELIF
# if idade >= 65:
#     print(f"\nO paciente {nome} POSSUI atendimento prioritário!\n")
# else:
#     print(f"\nO paciente {nome} NÃO possui atendimento prioritário!\n")

# ESTRUTURA DE DECISÃO COMPOSTA COM ELIF
if doenca_infectocontagiosa == "SIM" and idade >= 65:
    print(f"O paciente {nome} deve ser redirecionado para a sala AMARELA. - COM PRIORIDADE")
elif idade >= 65:
    print(f"O paciente {nome} deve ser redirecionado para a sala BRANCA - COM PRIORIDADE")
elif doenca_infectocontagiosa == "SIM":
    print(f"O paciente {nome} deve ser redirecionado para a sala AMARELA - SEM PRIORIDADE")
else:
    print(f"O paciente {nome} deve ser redirecionado para a sala BRANCA - SEM PRIORIDADE")
