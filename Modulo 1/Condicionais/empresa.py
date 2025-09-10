vendas = int(input("Digite o quanto você vendeu: "))
dias = int(input("Digite quantos dias você veio: "))

salario = 10000
if vendas >= 10.000 and dias >= 20:
    salario * 1.10
    print("Você recebeu um bonûs de 10%")
else:
    salario * 1.03
    print("Você recebeu um bonûs de 3%")