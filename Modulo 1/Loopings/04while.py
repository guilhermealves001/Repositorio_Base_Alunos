# Crie um código que converte dolar para real e vice-versa
# criar uma variável chamada cotação 
# solicitar ao usuário a coversao desejada
# apresente o resultado da conversão 
# perguntar se ele deseja continuar a conversão 

letra = 's'
while letra == 's':
    cotacao = float (input("Digite a cotação do dólar:"))
    print('-'*50)
    print(f"-"*15, "escolha a opção ",'-'*15)
    print('-'*50)

    opcao = int(input("1 - coverter dolar para real |2 - converter real para dólar"))

if opcao == 1:
    valor = float(input("Digite o valor em dolar a ser convertido para real U$:"))
    resultado = valor * cotacao
    print(f"O valor em reais é : {resultado:.2f}")
elif opcao == 2:
    valor1 = float(input("Digite o valor em real convertido para dólar R$:"))
    resultado1 = valor1/cotacao
    print(f"O valor em reais é : {resultado1:.2f}")
else:
    print("Digite uma opção válida")
letra = input("Deseja continuar ? (s/n):").lower()
