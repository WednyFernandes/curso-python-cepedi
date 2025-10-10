"""
Este programa coleta números digitados pelo usuário até que um valor de parada seja informado, e soma todos os valores inseridos.

Conceitos praticados:
- Listas
- Laço while
- Entrada de dados (input)
- Conversão de tipos
"""

numeroslista = []

parador = 1

somatotal = 0

print("Script coletor e somador de números inteiros")

while parador != 0:
    numero = int(input("Digite o número a ser somado (Use 0 para parar): "))
    if numero == 0:
        parador = 0
        break
    numeroslista.append(numero)

for item in numeroslista:
    somatotal += item

print(f"A soma total dos números digitados é: {somatotal}")
print(f"Números digitados: {numeroslista}")