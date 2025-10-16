import time

# Tempo inicial
inicio = time.time()

# Código a ser medido (exemplo: um loop)
for i in range(1000000):
    pass

# Tempo final
fim = time.time()

# Tempo decorrido
tempo_decorrido = fim - inicio
print(f"Tempo decorrido: {tempo_decorrido:.3f} segundos")