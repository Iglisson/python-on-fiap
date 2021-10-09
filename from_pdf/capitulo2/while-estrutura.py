#
numero = int(input("Digite um numero: "))

# vai verificar a condicao
while numero < 100:
    # caso a condicao seja verdadeira, o bloco abaixo sera executado
    print(f"\t {numero}")
    numero = numero + 1
    # ao fim do bloco, volta para o inicio e verifica se a condicao ainda esta verdadeira
print("PROGRAMA ENCERRADO!")