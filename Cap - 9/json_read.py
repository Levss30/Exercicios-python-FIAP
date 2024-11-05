import json

arquivo = open("c:\\arquivos\\dicionario.json", "r", encoding="UTF-8")

conteudo = arquivo.read()
agenda = json.loads(conteudo)

print(agenda)