"""
Este programa verifica duas condições:
1. Se o primeiro número é maior que 10.
2. Se a soma dos dois números é par ou ímpar.
Ele imprime os resultados das verificações.

Conceitos praticados:
- Entrada de dados (input)
- Conversão de tipos (float)
- Operações aritméticas
- Operadores de comparação
- Estruturas condicionais (if-else)
- Operadores lógicos (implicito no %)
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("A verificação do primeiro numero ser maior que 10: ", num1>10)
print("A verificação da soma dos números é par retorna: ", (num1+num2)%2 == 0)

if (num1+num2)%2 == 0:
    print("eh par")
else:
    print("eh impar")