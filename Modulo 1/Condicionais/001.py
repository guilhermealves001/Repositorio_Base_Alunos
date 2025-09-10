#1. Identificação de número, positivo, negativo ou zero
# Crie um código em python que leia o número e informe se ele é 
# positivo, negativo ou zero

#1) entrada de dados
num = int(input("Digite um número inteiro"))
#2) condicional para checar se o número é igual ou maior que zero
if num >= 0:
   #condicional para checar se o número é zero
    if num == 0:
        print("O número digitado é zero")
    else: #informa que o número é positivo
        print(f"O número {num} é positivo")
# se o of for falso, entra no else e informe que o número é negativo
else:
    print(f"O número é negativo")