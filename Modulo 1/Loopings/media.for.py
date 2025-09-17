# Solicite ao usuário 4 notas
# Calcule a média
# Informe se o aluno está aprovado (media >=7), recuperação(5<media<7)
# Ou reperovado e apresente as notas que o aluno tirou, 
# a media e o status da sua situação

#lista
# for
#if/elif/else

notas = 0
for i in range(0,4):
    nota = float(input("Digite sua nota: "))
    notas += nota / 4
if notas >=7:
    print(f"Você tirou {notas} passou de ano")
elif 5<=notas <7:
    print(f"Você tirou {notas} e está de recuperação")
else:
    print(f"Você tirou {notas} e reprovou")