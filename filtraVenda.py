lista_de_compras = []

for i in range(2):
    lista_de_compras.append(input("Insira um novo produto: "))

print(lista_de_compras)

while True:
    if input("Deseja remover algo? S | N ") in "Ss":
        item_remover = input("Qual item gostaria de remover? ")
        lista_de_compras.remove(item_remover)
        if len(lista_de_compras) == 0: print("Lista vazia"); break
        print(f"Lista atualizada: {lista_de_compras}")
    else:
        break 