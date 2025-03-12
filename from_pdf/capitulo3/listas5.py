# Situação 2: um equipamento com um determinado número serial foi danificado e será descartado. Precisamos eliminar esse equipamento. Dica: para eliminar um item de uma lista, você pode utilizar o comando “del”. Exemplo: del lista[<indice>]

equipamentos = ["Faca", "Tesoura", "Bola", "Impressora", "Impressora", "Martelo"]
valores = [14.9, 3.7, 59.9, 899.9, 1239.9, 39.9]
numeros_seriais = [1212121, 3141414, 4144141, 54476556, 74635423, 53543532]
departamentos = ["Utensílio", "Material escolar", "Esporte", "Informatica", "Informatica", "Material de construção"]

# Imprimir cada item da lista pelo indice
for indice in range(0, len(equipamentos)):
    print(f"Indice do produto: {indice}")
    print(f"Equipamento: {equipamentos[indice]}")
    print(f"Valor: {valores[indice]}")
    print(f"Número serial: {numeros_seriais[indice]}")
    print(f"Departamento: {departamentos[indice]}\n")

# deletando o equipamento desejado
deletar = int(input("Digite o indice do equipamento que voce deseja deletar: "))
equipamentos.pop(deletar)
valores.pop(deletar)
numeros_seriais.pop(deletar)
departamentos.pop(deletar)

# Imprimir cada item da lista pelo indice
for indice in range(0, len(equipamentos)):
    print(f"Indice do produto: {indice}")
    print(f"Equipamento: {equipamentos[indice]}")
    print(f"Valor: {valores[indice]}")
    print(f"Número serial: {numeros_seriais[indice]}")
    print(f"Departamento: {departamentos[indice]}\n")