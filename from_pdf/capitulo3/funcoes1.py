#
def preencher_inventario(lista):
    resposta = 's'
    while resposta == 's':
        equipamento = [
            input("Equipamento..: "),
            float(input("Valor........: ")),
            int(input("Número Serial: ")),
            input("Departamento.: ")
        ]
        lista.append(equipamento)
        resposta = input("Digite 's' para continuar: ").lower()
        print()

#
def exibir_inventario(lista):
    for elemento in lista:
        print(f"Equipamento.: {elemento[0]}")
        print(f"Valor.......: {elemento[1]}")
        print(f"Serial......: {elemento[2]}")
        print(f"Departamento: {elemento[3]}\n")

def localizar_nome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print(f"Valor.: {elemento[1]}")
            print(f"Serial: {elemento[2]}")

def depreciar_nome(lista, porcentagem):
    depreciar = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciar == elemento[0]:
            print(f"Antigo valor: {elemento[1]}")
            elemento[1] *= (1-porcentagem/100)
            print(f"Novo valor..: {elemento[1]}")

def deletar_serial(lista):
    serial = int("\nDigite o número serial do produto que será deletado: ")
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Item deletado"

def resumir_valores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print(f"O maior número da lista é: {max(valores)}")
        print(f"O menor número da lista é: {min(valores)}")
        print(f"A soma de todos os números da lista é: {sum(valores)}")