# Crie um código python que peça ao usuário 
# o código de um produto e informe o preço

print("Menu de produtos")
print("1- Café")
print("2- Chá")
print("3- Suco")
print("4- Refrigerante")
print("5- Água")

codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1:
        print("Produto: Café 500 g: R$ 36,00")
    case 2:
        print("Produto: Chá 100 g: R$ 8,00")
    case 3:
        print("Produto: Suco 1 L: R$ 16,00")
    case 4:
        print("Produto: Refrigerante 2 L: R$ 18,00")
    case 5:
        print("Produto: Água 500 ml: R$ 12,00")
    case _:
        print("Digite um código válido.")