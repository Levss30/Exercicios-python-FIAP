# Yoda
# Mace Windu
# Anakin Skywalker
# R2-D2
# Dex

dicionario = {
    "Yoda": "Mestre Jedi", 
    "Mace Windu": "Meste Jedi",
    "Anakin Skywalker": "Cavaleiro Jedi",
    "R2-D2": "Droid",
    "Dex": "Balconista"
}

# for chaves in dicionario.keys():
#     print(chaves)

# for valor in dicionario.values():
#     print(valor)

# print(dicionario["R2-D2"])

for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")