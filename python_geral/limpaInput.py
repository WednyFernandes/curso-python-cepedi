"""
Este programa solicita nome e email do usuário, aplica limpeza e formatação (maiúsculo, minúsculo, remoção de espaços) e imprime os valores processados.

Conceitos praticados:
- Entrada de dados (input)
- Manipulação de strings (upper, lower, strip, replace)
- Formatação de saída
"""

nome = input("Digite seu nome: ").upper().strip()
email = input("Digite seu email: ").lower().replace(" ", "").strip()

print(f"Nome: {nome} : E-mail: {email}")