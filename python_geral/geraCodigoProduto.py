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

# produtos = [
#     {"nome": "Apple iPhone 15 Pro", "ano": "2025"},
#     {"nome": "Samsung Galaxy S21 Ultra", "ano": "2024"},
#     {"nome": "Google Pixel 8 Pro", "ano": "2025"},
#     {"nome": "Xiaomi Redmi Note 13 Pro", "ano": "2024"},
#     {"nome": "OnePlus 12", "ano": "2025"}
# ]

# def criacodigocomplex(i):
#     fase1 = produtos[i]["nome"][:3] * 3
#     fase2 = produtos[i]["nome"][-4:]
#     fase3 = produtos[i]["nome"][2]
#     fase4 = produtos[i]["ano"][-2:]
#     final = (fase1 + fase2 + "-" + fase3 + fase4).upper()

#     ast = "*" * 20
#     print("\n")
#     print(f"{ast}")
#     print(f"Nome do produto: {produtos[i]["nome"]}")
#     print(f"Ano do produto: {produtos[i]["ano"]}")
#     print(f"Código gerado: {final}")
#     print(f"{ast}")
#     print("\n")

# index = int(input("Digite o index do produto: "))
# criacodigocomplex(index)