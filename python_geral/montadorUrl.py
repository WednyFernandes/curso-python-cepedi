"""
Este programa constrói uma URL completa solicitando caminhos (pastas) do usuário e juntando-os com um separador.
Ele solicita 3 caminhos e os combina em uma URL base.

Conceitos praticados:
- Listas
- Laços de repetição (for)
- Entrada de dados (input)
- Manipulação de strings (join)
"""

caminhos = []
final = ""
separador = "/"
x = 3
url = "https://dominio.com.br/"

for i in range(x):
    caminhos.append(input("Digite um caminho (Pasta): "))

final = separador.join(caminhos)

print(f"{url}{final}")