"""
Este programa simula um sistema de login simples com senha.
O usuário tem até 3 tentativas para acertar a senha correta.
Exibe mensagens de sucesso ou erro conforme as tentativas.

Conceitos praticados:
- Entrada de dados (input)
- Estruturas de repetição (while)
- Estruturas condicionais (if-else)
- Contadores e controle de fluxo
"""

senha = "python123"

max_tentativas = 3
erros = 0

while max_tentativas > 0:
    # Input da senha do usuário
    senhainserida = input("Digite a senha: ")

    # Verifica se a senha está correta
    if senhainserida == senha:
        print("Acesso liberado!")
        max_tentativas = 0
    else:
        erros += 1
        max_tentativas -= 1
        print(f"Senha incorreta. Tente novamente. Tentativas restantes: {max_tentativas}")

    # Conta os erros e bloqueia acesso após 3 erros    
    if erros >= 3:
        print("Conta bloqueada.")
        max_tentativas = 0
