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

# print(contatos.keys())
# print(contatos.values())
# print(contatos.items())

for nome, formas_contato in contatos.items():
    print(f"O contato {nome}")
    for forma, valor in formas_contato.items():
        print(f"Pode ser contatado pelo seu {forma} através do {valor}")