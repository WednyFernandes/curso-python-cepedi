"""
Este programa usa uma estrutura condicional if-else para verificar se a idade é maior ou igual a 18.
Dependendo da idade, imprime uma mensagem diferente.

Conceitos praticados:
- Entrada de dados (input)
- Conversão de tipos (int)
- Estruturas condicionais (if-else)
- Operadores de comparação
"""

idade = int(input("Fala tu menor qual tua idade na situação? "))

if(idade >= 18):
    print("Tu ta pro crime")
else:
    print("Tu não estás para o crime")