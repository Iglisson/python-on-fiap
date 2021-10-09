#
resposta = "SIM"
while resposta == "SIM":

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = ""

    # vai continuar a pergunta ate sair SIM ou NAO
    while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
        doenca_infectocontagiosa = input("Suspeita de doenca infectocontagiosa? [SIM ou NAO] > ").upper()

    # PRIMEIRO PROBLEMA A SER RESOLVIDO
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para a sala AMARELA!")
    else:
        print("Encaminhe o paciente para a sala BRANCA!")

    # SEGUNDO PROBLEMA A SER RESOLVIDO
    if idade >= 65:
        print("Paciente COM prioridade!")
    else:
        # TECEIRO PROBLEMA A SER RESOLVIDO
        genero = input("Qual o genero do paciente? [F ou M] > ").upper()
        if genero == "F" and idade > 10:
            gravidez = input("A paciente esta gravida? [SIM ou NAO] > ").upper()
            if gravidez == "SIM":
                print("Paciente COM prioridade!")
            else:
                print("Paciente SEM prioridade!")
        else:
            print("Paciente SEM prioridade!")
    
    # 
    resposta = input("\nDigite SIM para continuar: ").upper()