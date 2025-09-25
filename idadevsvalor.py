idade = int(input("Fala tu menor qual tua idade na situação? "))
valor = float(input("Qual o valor do produto que tu vende? "))

print("Tu é de maior?", idade>=18)
print("Teu produto vale merreca?", valor<50)

print("Operação combinada: ", idade>=18 and valor<50)