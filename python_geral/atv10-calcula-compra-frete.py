"""
Este programa calcula o valor total de um produto incluindo o frete baseado na região de entrega.
Ele solicita o nome do produto, seu valor e a região, e adiciona o custo do frete correspondente.

Conceitos praticados:
- Dicionários
- Entrada de dados (input)
- Funções
- Estruturas condicionais (if-else)
- Manipulação de strings (upper, strip)
"""

custo_frete = {
    "SUL": 15.00,
    "SUDESTE": 12.00,
    "NORDESTE": 20.00,
    "OUTRAS": 30.00
}

produto = input("Digite o nome do seu produto: ")
valor = float(input("Digite o valor do produto: "))
zona = input("Digite a sua região: ").upper().strip()

def calcula_frete():
    for i in custo_frete:
        if i == zona:
            return valor + custo_frete[i]
    return valor + custo_frete["OUTRAS"]

print(f"Seu produto {produto} | Custa R${valor}\nTotal R${calcula_frete()} com o frete para a sua região.")
