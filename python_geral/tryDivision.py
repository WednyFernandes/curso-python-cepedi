try:
    num1 = float(input("Qual valor?: "))
    num2 = float(input("Dividido pro quanto?: "))
    final = num1 / num2
    print(f"{num1} dividido por {num2}: {final}")
except ZeroDivisionError:
    print("Não é possivel dividir por zero")
except ValueError:
    print("Você não digitou um número válido")
except Exception as e:
    print(f"Erro inesperado: {e}")