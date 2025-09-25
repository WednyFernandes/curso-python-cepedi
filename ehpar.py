num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("A verificação do primeiro numero ser maior que 10: ", num1>10)
print("A verificação da soma dos números é par retorna: ", (num1+num2)%2 == 0)

if (num1+num2)%2 == 0:
    print("eh par")
else:
    print("eh impar")