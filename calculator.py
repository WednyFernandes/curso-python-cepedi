multiplicacao = "*"
divisao = "/"
soma = "+"
subtracao = "-"

num1 = None
num2 = None

def calcular():
    print("Bem vindx à calculadora Python")
    resposta = input("Digite sua operação: ")
    if multiplicacao in resposta:
        valores = resposta.split(multiplicacao)
        num1 = valores[0]
        num2 = valores[1]
        print("Resultado",float(num1)*float(num2))
    elif divisao in resposta:
        valores = resposta.split(divisao,1)
        num1 = valores[0] 
        print(num1)
        num2 = valores[1]
        print(num2)
        if num1 == None or num2 == None:
            print("Operação invalida") 
        elif isinstance(num1,str) or isinstance(num2,str):
            print("Operação invalida")   
        else:      
            print("Resultado",float(num1)/float(num2))
    elif soma in resposta:
        valores = resposta.split(soma)
        num1 = valores[0]
        num2 = valores[1]
        if num1 == None or num2 == None:
            print("Operação invalida") 
        elif isinstance(num1,str) or isinstance(num2,str):
            print("Operação invalida")   
        else:       
            print("Resultado",float(num1)+float(num2))
    elif subtracao in resposta:
        valores = resposta.split(subtracao)
        num1 = valores[0]
        num2 = valores[1]
        if num1 == None or num2 == None:
            print("Operação invalida") 
        elif isinstance(num1,str) or isinstance(num2,str):
            print("Operação invalida")   
        else:  
            print("Resultado",float(num1)-float(num2))

    if int(input("Deseja continuar? 1 - SIM | 2 - NÃO: ")) == 1:
        calcular()
    else:
        quit()
        
calcular()