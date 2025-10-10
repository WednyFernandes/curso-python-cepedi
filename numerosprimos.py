"""
Este programa identifica números primos em um intervalo informado pelo usuário.

Conceitos praticados:
- Entrada de dados (input)
- Laço for
- Listas
- Estruturas condicionais
"""

import time

primos = []

primero_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

print("Calculando...")
time.sleep(2)

for num in range(primero_numero, segundo_numero + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primos.append(num)

print(f"Números primos entre {primero_numero} e {segundo_numero}:\n{primos}")
print(f"Total de números primos encontrados: {len(primos)}")