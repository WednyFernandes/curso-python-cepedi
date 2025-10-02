numero = int(input("Digite um número: "))
soma = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        soma += i
print("A soma dos números pares de 1 até", numero, "é:", soma)

print("São eles:")

soma = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        soma += i
        print(f"Proximo par: {i}")
        print(f"Soma até agora {soma - i} + {i} = {soma}")