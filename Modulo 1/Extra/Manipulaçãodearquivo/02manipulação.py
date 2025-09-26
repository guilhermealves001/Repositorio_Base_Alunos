arquivo = open("pessoa.txt", "r") # a leitura estás endo feita na memória
conteudo = arquivo.read()
print(conteudo)
arquivo.close()