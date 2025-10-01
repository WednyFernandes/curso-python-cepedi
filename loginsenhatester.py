senha = "python123"

tentativas = 3
erros = 0

while tentativas > 0:
    # Input da senha do usuário
    senhainserida = input("Digite a senha: ")

    # Verifica se a senha está correta
    if senhainserida == senha:
        print("Acesso liberado!")
        tentativas = 0
    else:
        erros += 1
        tentativas -= 1
        print(f"Senha incorreta. Tente novamente. Tentativas restantes: {tentativas}")

    # Conta os erros e bloqueia acesso após 3 erros    
    if erros >= 3:
        print("Conta bloqueada.")
        tentativas = 0       