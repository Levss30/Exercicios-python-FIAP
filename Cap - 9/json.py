import json

contatos = {
    "Clark Kent": {
        "celular": "11957483726",
        "email": "Clark@krypto.com"
    },
    "Bruce Wayne": {
        "celular": "11382948576",
        "email": "Bat@caverna.com"
    },
}

# print(json.dumps(contatos, indent=4))

arquivo = open("c:\\arquivos\\dicionario.json", "w", encoding="UTF-8")

conteudo = json.dumps(contatos, indent=4)
arquivo.write(conteudo)