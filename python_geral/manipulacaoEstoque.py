"""
Este programa manipula uma lista de estoque, permitindo adicionar novos itens e exibir a lista atualizada.

Conceitos praticados:
- Listas
- Métodos de listas (append)
- Entrada de dados (input)
- Função print()
"""

estoque = ["Labubu","Bobbie Goods","Metanol"]
print(f"\nLista atual: {estoque}")


estoque.append(input("\nInsira um novo item maravilhoso nessa lista: "))
print(f"\nLista atual: {estoque} \nItem adicionado: {estoque[-1]}")


estoque.insert(0, input("\nDigite um número: "))
print(f"\nLista atual: {estoque}")


estoque.remove(input("\nAgora insira um item para retirarmos: "))
print(f"\nLista atual: {estoque}")