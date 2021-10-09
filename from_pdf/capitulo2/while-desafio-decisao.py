#
resposta = "SIM"
while resposta == "SIM":

    nivel_acesso = input("Qual o seu nivel de acesso [ADM, USR ou GUEST] > ").upper()

    if nivel_acesso == "ADM" or nivel_acesso == "USR":
        
        genero = input("Digite o seu genero [FEMININO ou MASCULINO] > ").upper()
        
        if nivel_acesso == "ADM":
            if genero == "FEMININO":
                print("Seja bem vinda Aministradora!")
            elif genero == "MASCULINO":
                print("Seja bem vindo Administrador!")
            else:
                print("Fora do escopo do sistema!")

        else:
            if genero == "FEMININO":
                print("Seja bem vinda, Usuaria!")
            elif genero == "MASCULINO":
                print("Seja bem vindo, Usuario!")
            else:
                print("Fora do escopo do sistema!")

    elif nivel_acesso == "GUEST":
        print("Ola visitante.")
        
    else:
        print("Ola desconhecido(a).")

    resposta = input("\nDigite SIM se deseja continuar: ").upper()