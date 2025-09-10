# Peça ao usuário para digitar uma letra 
# Se for vogal, informe qual
# Se for consoante, verifiqye se é maiuscula ou minuscula

# Solicitação de entrada de dados 
letra = input("Digite uma letra: ")

if letra.lower () in "aeiou": # .lower() transforma para minuscula
    print(f"Vogal: {letra}")
else:
    if letra.isupper():  # isupper identifica se a letra está em maiúscula 
        print("Consoante maiúscula.")
    else:
        print("Consoante minúscula.")