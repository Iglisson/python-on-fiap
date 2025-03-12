# Listas de Listas
produtos = []

resposta = 's'
respostas = ['sim', 'si', 's', 'yes', 'y']

while resposta in respostas:
    produto = []
    produto.append(input('Equipamento: '))
    produto.append(float(input('Valor: ')))
    produto.append(int(input('Número serial: ')))
    produto.append(input('Departamento: '))

    # Adiciona os produto na lista de produtos
    produtos.append(produto)
    resposta = input("Digite 'S' para continuar: ").lower()
    print()

for elemento in produtos:
    print(elemento)