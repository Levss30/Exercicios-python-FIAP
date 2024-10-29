# def somar():
#     valor1 = int(input("Digite um valor: "))
#     valor2 = int(input("Digite outro valor: "))
#     soma = valor1 + valor2
    
#     print(f"O valor da soma é:  {soma}")
    
# somar()

def somar(valor1, valor2):
    soma = valor1 + valor2
    # print(soma)
    return soma
    
primeiro_valor = float(input("Informe um valor: "))
segundo_valor = float(input("Informe o segundo valor: "))
soma = somar(primeiro_valor, segundo_valor)
media = soma/2

print(media)