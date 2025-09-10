#2. Paridade e tamanho de número 
# Crie um código que receba um número inteiro e informe:
# - se é par ou ímpar
# -e, ao mesmo tempo se é maior que 10 ou menor ou igual a 10
#Utilize condicionais aninhadas para organizar as verificações

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    if num >=10:    
        print(f"O número é par e maior que dez.")
    else: 
        print(f"O número é par e menor que dez. ") 
else:       
     if num >=10:   
        print(f"O número é ímpar e menor que dez. ")  
     else:
        print("O número é ímpar e maior que dez.")       
