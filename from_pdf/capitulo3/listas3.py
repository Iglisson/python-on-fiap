# Multiplas Listas

equipamentos = []
valores = []
numeros_seriais = []
departamentos = []

resposta = 's'
respostas = ['sim', 'si', 's', 'yes', 'y']

while resposta in respostas:
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    numeros_seriais.append(int(input('Número serial: ')))
    departamentos.append(input('Departamento: '))

    # Adiciona os produto na lista de produtos
    resposta = input("Digite 'S' para continuar: ").lower()
    print()

# Imprimir cada item da lista pelo indice
for indice in range(0, len(equipamentos)):
    print(f"Equipamento: {equipamentos[indice]}")
    print(f"Valor: {valores[indice]}")
    print(f"Número serial: {numeros_seriais[indice]}")
    print(f"Departamento: {departamentos[indice]}\n")