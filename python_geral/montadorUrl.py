caminhos = []
final = ""
separador = "/"
x = 3
url = "https://dominio.com.br/"

for i in range(x):
    caminhos.append(input("Digite um caminho (Pasta): "))

final = separador.join(caminhos)

print(f"{url}{final}")