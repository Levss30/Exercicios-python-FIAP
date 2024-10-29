#Pedir que o usuário digite o nome do funcionário
nome = input("Informe o nome do funcionário: ")
#Pedir que o usuário digite o salário do funcionário
salario = float(input("Informe o salário do funcionario: "))
#Caso o salário seja negativo, alertar o usuário
if salario < 0:
    #salario = salario * -1
    #salario = abs(salario)
    print("Atenção, foi informado um salário negativo")

#Exibir o salário armazenado
print(f"O funcionario {nome} tem um salário de R${salario}")