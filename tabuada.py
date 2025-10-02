começo = int(input("Digite o número inicial para ver a tabuada: "))
final = int(input("Digite o número final da tabuada: "))

for i in range(começo, final + 1):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")