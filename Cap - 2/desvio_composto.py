#Pedir a idade do aluno
idade = int(input("Por favor, digite a idade do aluno: "))
#Verificar se o aluno é maior de idade ou menor de idade
if idade >= 18:
    print("O aluno é maior de idade")
elif idade < 18:
    print("O aluno é menor de idade")