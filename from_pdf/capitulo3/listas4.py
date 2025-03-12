# Situação 1: todos os equipamentos “impressora” receberão uma depreciação (desvalorização após certo período) de 10%. Monte o código que seria responsável por alterar o valor de todos os equipamentos “impressora”

equipamentos = ["Faca", "Tesoura", "Bola", "Impressora", "Impressora", "Martelo"]
valores = [14.9, 3.7, 59.9, 899.9, 1239.9, 39.9]
numeros_seriais = [1212121, 3141414, 4144141, 54476556, 74635423, 53543532]
departamentos = ["Utensílio", "Material escolar", "Esporte", "Informatica", "Informatica", "Material de construção"]

# Imprimindo todos os equipamentos antes da desvalorização
for indice in range(0, len(equipamentos)):
    print(f"Equipamento: {equipamentos[indice]}")
    print(f"Valor: R$ {valores[indice]}")
    print(f"Número serial: {numeros_seriais[indice]}")
    print(f"Departamento: {departamentos[indice]}\n")

# Depreciando as impressoras
for indice in range(0, len(equipamentos)):
    if equipamentos[indice] == "Impressora":
        valores[indice] *= 0.9

# Imprimindo valores depois de alterados
for indice in range(0, len(equipamentos)):
    print(f"Equipamento: {equipamentos[indice]}")
    print(f"Valor: R$ {valores[indice]}")
    print(f"Número serial: {numeros_seriais[indice]}")
    print(f"Departamento: {departamentos[indice]}\n")