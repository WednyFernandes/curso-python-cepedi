lado1 = float(input("Digite o tamanho do lado 1: "))
lado2 = float(input("Digite o tamanho do lado 2: "))
lado3 = float(input("Digite o tamanho do lado 3: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")