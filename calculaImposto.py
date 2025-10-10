valor_digitado = 0
imposto_digitado = 0

def digita_valor(): 
    valor_digitado = float(input("Digite o valor da venda: "))
    print('\033[1A' + '\033[K', end='')
    print(f"Valor: {valor_digitado}")
    imposto_digitado = float(input("Digite a porcentagem do imposto: "))
    print('\033[1A' + '\033[K', end='')
    print(f"Porcentagem do imposto: {imposto_digitado}")
    return valor_digitado, imposto_digitado

def calcular_imposto(valor,imposto):
    if imposto>=valor: 
        print("Digite denovo")
        valor, imposto = digita_valor()
        return calcular_imposto(valor,imposto)        
    else:
        return valor / imposto
    
valor_digitado, imposto_digitado = digita_valor()

print(f"O imposto do valor é: R${calcular_imposto(valor_digitado,imposto_digitado):.2f}")