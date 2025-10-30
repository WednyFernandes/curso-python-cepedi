def validar_idade():
    msgvalidadora = "a idade não pode ser negativa ou zerada!"
    
    try:
        idade = int(input("Digite sua idade: "))
        if(idade<=0):
            raise ValueError(msgvalidadora)
        else:
            print(f'Idade válida')
    except ValueError as e:
        if str(e) == msgvalidadora:
            print(f'Digite novamente, {e}')
        else:
            print(f"Erro de caracter: {e}")
        validar_idade()
    except Exception as f:
        print(f"Erro desconhecido: {e}")

validar_idade()
