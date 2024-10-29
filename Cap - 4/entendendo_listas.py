lista_instrumento = ["Bateria", "Guitarra", "Violão", "Guitarra", "Baixo"]

print(lista_instrumento)

# lista_instrumento.append(input("Insira algum instrumento: "))

# lista_instrumento.insert(0, "Violino")

# for instrumento in lista_instrumento:
#     print(instrumento)

# lista_instrumento.pop(0)

# lista_instrumento.remove("Guitarra")

# print(lista_instrumento)

# Qual é o tamanho da minha lista ?
print(len(lista_instrumento))

# Quantas vezes o elemento "Guitarra" aparece ?
print(lista_instrumento.count("Guitarra"))

# Como alterar a ordem dos elementos ?
lista_instrumento.reverse()
print(lista_instrumento)

# Como ordenar a lista em ordem crescente ?
lista_instrumento.sort()
print(lista_instrumento)

# Como ordenar a lista em ordem decrescente ?
lista_instrumento.sort(reverse=True)
print(lista_instrumento)