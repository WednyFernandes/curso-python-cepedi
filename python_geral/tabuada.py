"""
Este programa imprime a tabuada de multiplicação para um intervalo de números informado pelo usuário.

Conceitos praticados:
- Laço for
- Entrada de dados (input)
- Operações aritméticas
- Função print()
"""

começo = int(input("Digite o número inicial para ver a tabuada: "))
final = int(input("Digite o número final da tabuada: "))

for i in range(começo, final + 1):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

if final < começo:
    for i in reversed(range(final, começo + 1)):
        print(f"\nTabuada do {i} (de trás para frente):")
        for j in (range(1, 11)):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")