# Crie um programa que leia o peso de 5 pessoas e no final
# informe quem ´pe o mais leve e o mais pesado
# etapas para a resolução
# 1) crie uma lista vazia 
# 2) crie um for para receber o peso de 5 pessoas
# 3) Adicione os pesos a lista e ordene-os de maior para menor

pesos = []
for i in range(5):
    peso = float(input("Digite seu peso em kg: "))
    pesos.append(peso)
    print(f"A lista dos pesos em kg: ")
pesos.sort()
maior_peso = max(pesos)
menor_peso = min(pesos)   
print(f"O maior peso é {maior_peso} Kg e o menor peso é {menor_peso} Kg")