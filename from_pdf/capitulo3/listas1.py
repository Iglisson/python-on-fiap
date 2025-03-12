# Declaração de listas

## Lista preenchida estaticamente
# lista_estatica = ["carro", True]

## Lista preenchida dinâmicamente
# lista_dinamica = [input("Digite o nome de usuário: "), bool(int(input("Está logado? ")))]

## Lista vaziza
# lista_vazia = []

# Adicionando dados em uma lista de maneira indeterminada

inventario = []
respostas = ['sim', 'si', 's', 'yes', 'y']
resposta = 's'
while resposta in respostas:
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").lower()

for elemento in inventario:
    print(elemento)