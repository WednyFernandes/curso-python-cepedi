"""
Este programa gera um código único para um produto baseado no nome e ano.
Ele extrai partes do nome do produto e combina com o ano para formar um código.

Conceitos praticados:
- Manipulação de strings (fatiamento)
- Funções
- Formatação de saída
"""

nome_produto = "SMARTPHONE GALAXY S21"
ano_produto =  "2025"

def criacodigo():
    fase1 = nome_produto[:3] * 3
    fase2 = nome_produto[-4:]
    fase3 = nome_produto[2]
    fase4 = ano_produto[-2:]
    final = fase1 + fase2 + "-" + fase3 + fase4
    return final

def imprimecodigo():
    ast = "*" * 20

    print("\n")
    print(f"{ast}")
    print(f"Nome do produto: {nome_produto}")
    print(f"Ano do produto: {ano_produto}")
    print(f"Código gerado: {criacodigo()}")
    print(f"{ast}")
    print("\n")

imprimecodigo()
