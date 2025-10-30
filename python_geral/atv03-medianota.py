"""
Este programa calcula a média de três notas inseridas pelo usuário, com validação para garantir que as notas estejam entre 0 e 10.
Ele determina o status do aluno baseado na média:
- Aprovado se média >= 7
- Recuperação se 5 <= média < 7
- Reprovado se média < 5
Imprime o status com a média formatada.

Conceitos praticados:
- Listas
- Loops (for, while)
- Entrada de dados (input)
- Conversão de tipos (float)
- Validação de entrada
- Operações aritméticas (sum, len)
- Estruturas condicionais (if-elif-else)
- Formatação de saída (format, f-strings)
"""

notas = []
for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota? "))
    while nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        nota = float(input(f"Digite a {i}ª nota? "))
    notas.append(nota)
    
media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado com média", format(media, '.2f'))
elif media >= 5:
    print("Recuperação com média", format(media, '.2f'))
else:
    print("Reprovado com média", format(media, '.2f'))
