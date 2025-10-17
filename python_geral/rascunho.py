# Define uma classe de erro personalizada
class ValorIncorretoError(Exception):
    pass

# Define um valor negativo
valor = -100

# Tenta executar o código
try:
    # Verifica se o valor é menor ou igual a zero
    if valor <= 0:
        # Lança a exceção personalizada se o valor for incorreto
        raise ValorIncorretoError("Valor incorreto!")
# Captura a exceção personalizada
except ValorIncorretoError as e:
    # Imprime a mensagem de erro
    print(e)