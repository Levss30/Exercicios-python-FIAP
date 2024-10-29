# resposta = ""

# while resposta != "42":
#     resposta = input("Digite a resposta para a vida, universo e tudo mais! ")
    
# print("Parabéns, você é um verdadeiro geek! ")

# numero = 1

# while numero % 2 != 0:
#     numero = int(input("Por favor, informe um número par! "))
    
# print("Parabéns, o número informado é par! ")

i = 1
numero = int(input("Por favor, informe o valor do qual deseja a tabuada: "))

while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i = i + 1