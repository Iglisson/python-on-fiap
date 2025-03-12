from funcoes1 import *

minha_lista = []
print('Preenchendo lista...')
preencher_inventario(minha_lista)
print('Exibindo lista...')
exibir_inventario(minha_lista)

print("Pesquisando")
localizar_nome(minha_lista)
print("Alterando")
depreciar_nome(minha_lista, 20)
print("Excluindo")
print(deletar_serial(minha_lista))
exibir_inventario(minha_lista)
print("Resumindo")
resumir_valores(minha_lista)
