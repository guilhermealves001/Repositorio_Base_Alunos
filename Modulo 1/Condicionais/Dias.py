print("Dias da semana")
print(""" 1- Domingo
      2- Segunda
      3- terça
      4- quarta
      5- quinta
      6- sexta
      7- sabado""")

dia = int(input("Dígite um número de 1 a 7: "))

match dia:
    case 2|3|4|5|6:
        print("Não é final de semana.")
    case 1|7: 
        print("É final de semana.")
    case _:
        print("Número inválido.")