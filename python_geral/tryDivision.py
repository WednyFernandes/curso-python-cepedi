try:
    num1 = int(input("Qual valor?: "))
    num2 = int(input("Dividido pro quanto?: "))
    final = num1 / num2
    print(f"{num1} dividido por {num2}: {final}")
except ZeroDivisionError:
    print("Não é possivel dividir por zero")
except ValueError:
    print("Você digitou um número inválido ou não número")