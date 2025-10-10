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
    match zona:
        case custo_frete
    return

print(f"Seu produto {produto}, custa {valor} e sai a {valorcomfrete} com o frete.")