nomes = ['joão\n','maria\n', 'ana\n']

with open('nomes.txt', 'w', encoding = 'utf-8') as arquivo:

    arquivo.writelines(nomes)
