# VARIAVEIS
nome = input("Digite o nome: ").capitalize()
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? [SIM ou NAO] -> ").upper()

# ESTRUTURA DE DECISÃO ENCADEADA (sem uso de logicos)
if doenca_infectocontagiosa == "SIM":
    if idade >= 65:
        print(f"Paciente {nome} deve ser redirecionado para a sala AMARELA! - COM PRIORIDADE")
    else:
        print(f"Paciente {nome} deve ser redirecionado para a sala AMARELA! - SEM PRIORIDADE")
elif doenca_infectocontagiosa == "NAO":
    if idade >= 65:
        print(f"Paciente {nome} deve ser redirecionado para a sala BRANCA! - COM PRIORIDADE")
    else:
        print(f"Paciente {nome} deve ser redirecionado para a sala BRANCA! - SEM PRIORIDADE")
else:
    print("Responda a a suspeita de doença infectocontagiosa com SIM ou NAO!")
