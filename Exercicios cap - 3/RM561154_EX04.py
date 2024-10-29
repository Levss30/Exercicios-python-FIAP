#RM561154
#NOME: LUCAS ANDRES FRANÇA LAILHACAR LEVASSEUR

def calc_imposto (tipo_invest, valor_resgate, dias_invest):

    if tipo_invest == 1:
        if dias_invest <= 180:
            aliquota = 22.5 / 100
        elif 181 <= dias_invest <= 360:
            aliquota = 20 / 100
        elif 361 <= dias_invest <= 720:
            aliquota = 17.5 / 100
        else:
            aliquota = 15 / 100
        
        imposto = valor_resgate * aliquota
        return imposto
    

    elif tipo_invest in [2, 3]:
        return 0.0

print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

tp_investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))
valor_resgate = float(input("Digite o valor a ser resgatado: "))
d_investido = int(input("Digite o número de dias que o valor permaneceu investido: "))


if tp_investimento not in [1, 2, 3]:
    print("Tipo de investimento inválido.")
else:

    imposto = calc_imposto(tp_investimento, valor_resgate, d_investido)

    print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")
