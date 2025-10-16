"""
Este programa checa se uma pessoa é maior ou menor de idade, recebendo nome e idade em um loop.
Permite encerrar digitando 00 em qualquer campo.

Conceitos praticados:
- Funções
- Estruturas condicionais (if-else)
- Entrada de dados (input)
- Conversão de tipos (int)
- Laço while
"""

print("Bem vindo ao checador de maioridade \nDigite 00 em qualquer campo para encerrar")
nomeG = None
idadeG = None

def checar_idade(nome, idade):
    if idade >= 18:
        print(f"{nome} é MAIOR de idade!")
    else:
        print(f"{nome} é MENOR de idade!")

def parador(n,i):
    if n == "00" or i == 00:
        print("Encerrando programa.")
        return True    

while True:
    nomeG = input("Insira o nome da pessoa: ")
    if parador(nomeG,idadeG): break
    idadeG = int(input("Insira a idade da pessoa: "))
    if parador(nomeG,idadeG): break
    checar_idade(nomeG,idadeG)