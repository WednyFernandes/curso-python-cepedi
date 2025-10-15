nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

nome = nome.upper().strip()
email = email.lower().replace(" ", "").strip()

print(f"Nome: {nome} : E-mail: {email}")