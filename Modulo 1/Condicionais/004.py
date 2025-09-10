# Tipo de triangulo 
# crie um programa que receba tres lados de um triangulo
# verifique se os lados realmente podem formar um triangulo
# e determine os triangulos em:
# equilatero ( todos lados iguais)
# isoceles (dois lados iguais)
# escaleno (todos os lados diferentes)

a = int(input("Digite o valor do lado de um triangulo a:"))
b = int(input("Digite o valor do lado de um triangulo b:"))
c = int(input("Digite o valor do lado de um triangulo c:"))

if a + b > c and a + c > b and b + c > a:
    if a == b:
        if b == c:
            print(f"Os lados do triângulo são {a}, {b} {c}: Triângulo equilatero")
else:
    print("Os lados do triângulo são {a}, {b} {c}: Triângulo isósceles")
    if b == c or a == c:
        print("Os lados do triângulo são {a}, {b} {c}: Triangulo escaleno")
    else:
        print("Os lados de um triângulo válido")
