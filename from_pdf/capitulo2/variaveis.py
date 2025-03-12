# DECLARANDO VARIAVEIS e ATRIBUINDO DADOS
# nome = "Iglisson Ruan"
# universidade = 'UEPA'
# semestre = 5
# saldo_bancario = 5.78

# ATRIBUINDO VALORES COM O PROGRAMA EM EXECUÇÃO
nome = input("Digite o nome do aluno: ")
universidade = input("Digite qual a universidade que ele frequenta? ")
semestre = int(input("Digite qual o semestre que ele está: "))
saldo_bancario = float(input("Digite o saldo bancario dele: "))

# IMPRIMINDO VALORES
print(f"\n{nome.capitalize()} estuda na {universidade.upper()} e está no {semestre}º semestre")
print("Saldo bancario: R$" + str(saldo_bancario))

# EXIBINDO O TIPO DA VARIAVEL
print("\n----------TIPOS DAS VARIAVEIS----------")
print(f"A variavel [nome] é do tipo {type(nome)}")
print(f"A variavel [universidade] é do tipo {type(universidade)}")
print(f"A variavel [semestre] é do tipo {type(semestre)}")
print(f"A variavel [saldo_bancario] é do tipo {type(saldo_bancario)}")
