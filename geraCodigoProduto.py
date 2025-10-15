nome_produto = "SMARTPHONE GALAXY S21"
ano_produto =  "2025"

def criacodigo():
    fase1 = nome_produto[:2] * 3
    fase2 = nome_produto[-4:].strip()
    fase3 = nome_produto[2]
    fase4 = ano_produto[-2:]
    final = fase1 + fase2 + fase3 + "-" + fase4
    return final

def imprimecodigo():
    ast = "*" * 20

    print("\n\n")
    print(f"{ast}")
    print(f"Nome do produto: {nome_produto}")
    print(f"Ano do produto: {ano_produto}")
    print(f"Código gerado: {criacodigo()}")
    print(f"{ast}")
    print("\n\n")

imprimecodigo()