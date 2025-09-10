# Crie um código python utilizando match case que
# solicirte ao usuário o tipo de pizza desejada e informe o preço

print("Menu Pizzaria")
print("1- Marguerita")
print("2- Frango com catupiry")
print("3- Quatro queijos")
print("4- Portuguesa") 
print("5- Calabresa")

pizza = int(input("Qual pizza você gostaria: "))

match pizza:
    case 1:
        print("1- Marguerita| R$ 50,00")
    case 2:
        print("2- Frango com catupiry| R$ 60,00")
    case 3:
        print("3- Quatro queijos| R$ 65,00")
    case 4:
        print("4- Portuguesa| R$ 68,00")
    case 5:
        print("5- Calabresa| R$ 56,00")
    case _:
        print("Digite um código válido.")