"""
Este programa manipula uma lista de notas e calcula a média das três últimas.

Conceitos praticados:
- Listas
- Fatiamento de listas
- Cálculo de média
"""

notas = [1,2.5,2,7,9.5]
ultimas_tres = notas[-3:]
media = 0
soma = 0

print(f"Ultimas notas: {ultimas_tres}")

for item in ultimas_tres:
    soma += item

media = soma/3

print(f"A média das 3 ultimas nota é: {media}")