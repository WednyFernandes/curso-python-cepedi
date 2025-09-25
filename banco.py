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