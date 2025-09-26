with open('pessoa.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    print('total linhas:', len(linhas))