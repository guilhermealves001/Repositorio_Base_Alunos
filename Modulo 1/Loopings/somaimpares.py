# Cruie um programa que some todos os números ímpares
#que são múltiplos de 3 e 1 a 30 e apresente o resultado 

# etapas para resolução 
# 1) criar um for de para captar os números ímpares 
# 2) criar uma condicional para checar se o número é múltiplo de 3
# 3) somar os números que atendem a condicional 
# 4) apresentar os resultados 

multiplo_tres = 0 
for i in  range(1,31,2):
    if i % 3 ==0:
        print(i, end=',')

        multiplo_tres += i
print()
print(f"A soma dos números ímapres múltiplos de 3 é {multiplo_tres}")

