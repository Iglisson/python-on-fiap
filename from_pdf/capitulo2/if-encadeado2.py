#
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? [SIM ou NAO] > ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para a sala AMARELA!")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente para a sala BRANCA!")
else:
    print("Responda sobre a suspeita de doenca infectocontagiosa com SIM ou NAO!")
    exit() # ENCERRA O PROGRAMA

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade!")
else:
    # TECEIRO PROBLEMA A SER RESOLVIDO
    genero = input("Qual o genero do paciente? [F ou M] > ").upper()
    if genero == "F" and idade > 10:
        gravidez = input("A paciente esta gravida? [SIM ou NAO]").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade!")
        else:
            print("Paciente SEM prioridade!")
    else:
        print("Paciente SEM prioridade!")
