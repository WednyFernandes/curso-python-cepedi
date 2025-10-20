"""
Este programa simula um sistema de login bancário simples.
Ele verifica se o usuário e senha fornecidos correspondem a um dos usuários cadastrados em uma lista.
Se o login for bem-sucedido, chama uma função para operações bancárias (ainda não implementada).

Conceitos praticados:
- Listas e dicionários
- Loops (for)
- Entrada de dados (input)
- Estruturas condicionais (if-else)
- Funções
"""

def rodar_banco():
    print("operações bancárias")
    return None

usuarios = [
    {"nome": "Wedny", "senha": "123"},
    {"nome": "Keil", "senha": "456"},
    {"nome": "Pedro", "senha": "789"},
    {"nome": "Ana", "senha": "111"},
    {"nome": "Lucas", "senha": "222"}]

login_user = input("Digite seu usuario: ")
login_senha = input("Digite sua senha: ")

logado = False

for item in usuarios:
    if login_user == item["nome"] and login_senha == item["senha"]:
        logado = True
        print("Login bem-sucedido!")
        break 
    
if not logado:
    print("Usuário ou senha inválidos.")

print(f"Status de login: {logado}")

if(logado):
    rodar_banco()