"""
Este programa verifica se a idade é maior ou igual a 18 e se o valor do produto é menor que 50.
Ele imprime os resultados booleanos das comparações e uma operação combinada com 'and'.

Conceitos praticados:
- Entrada de dados (input)
- Conversão de tipos (int, float)
- Operadores de comparação
- Operadores lógicos (and)
- Função print()
"""

idade = int(input("Fala tu menor qual tua idade na situação? "))
valor = float(input("Qual o valor do produto que tu vende? "))

print("Tu é de maior?", idade>=18)
print("Teu produto vale merreca?", valor<50)

print("Operação combinada: ", idade>=18 and valor<50)