#\

# arquivo = open("c:\\arquivos\\dicionario.txt", encoding="UTF-8")
arquivo = open("./arquivo.txt", encoding="UTF-8")

# print(arquivo.readline())
# print(arquivo.readline())

for linha in arquivo.readlines():
    print(linha)
    
arquivo.close()