dicionario = {
}

#Adicionando os dados
dicionario["Lucas Andres"] = "Aluno da FIAP"

#Adicionando os dados
nome_colaborador = input("Por favor, informe o nome do colaborador: ")
cargo_colaborador = input("Por favor, informe o cargo do colaborador: ")
dicionario[nome_colaborador] = cargo_colaborador



for nome, cargo in dicionario.items():
    print(f"O colaborador {nome} atua no cargo de {cargo}")
    
#Alterando os dados
dicionario["Lucas Andres"] = "Cordenador da FIAP"

for nome, cargo in dicionario.items():
    print(f"O colaborador {nome} atua no cargo de {cargo}")

#Deletar o dado
dicionario.pop("Lucas Andres")

for nome, cargo in dicionario.items():
    print(f"O colaborador {nome} atua no cargo de {cargo}")
    
#Remover o ultimo item do dicionario:
dicionario.popitem()

