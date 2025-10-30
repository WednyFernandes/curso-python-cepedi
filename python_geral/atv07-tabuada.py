"""
Este programa imprime a tabuada de multiplicação para um intervalo de números informado pelo usuário.

Conceitos praticados:
- Laço for
- Entrada de dados (input)
- Operações aritméticas
- Função print()
"""

comeco = int(input("Digite o número inicial para ver a tabuada: "))
final = int(input("Digite o número final da tabuada: "))

for i in range(comeco, final + 1):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

if final < comeco:
    for i in reversed(range(final, comeco + 1)):
        print(f"\nTabuada do {i} (de trás para frente):")
        for j in (range(1, 11)):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
