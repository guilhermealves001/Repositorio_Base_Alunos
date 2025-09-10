#3. Classificação por idade 
# Faça um programa que leia a idade de uma pessoa e classifique-a em:
#criança: menor de 12 anos
#adolescente: entre 12 e 17
#adulto: igual ou maior de 18
# Utilize a estrutura de condicional aninhada 

idade = int(input("Digite sua idade: "))
if idade > 18:
    print("Você é adulto.")
elif 12 <= idade <= 17:
        print("Você é adolescente.")
else:
     if idade <12:
         print("Você é criança.")       
