# Crie um programa que:
# 1) Peça ao usuário que divide um número de 1 a 7 
# para indicar os dias da semana 
# 2) Use match case para exibir o nome correspondente ao número:
# 1 - domingo
# 2 - Segunda
# 3 - terça
# 4 - quarta
# 5 - quinta
# 6 - sexta 
# 7 - sabado

dia = int(input("Dígite um número de 1 a 7: "))

match dia:
    case 1:
        print("É domingo. Boa semana")
    case 2:
        print("Hoje é segunda. Boa semana.") 
    case 3:
        print("Hoje é terça.") 
    case 4:
        print("Hoje é quarta.") 
    case 5:
        print("Hoje é quinta.")
    case 6:
        print("Hoje é sexta")
    case 7:
        print("Hoje é sábado.")
    case _:
        print("Número inválido.")