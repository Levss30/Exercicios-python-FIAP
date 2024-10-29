#RM561154
#NOME: LUCAS ANDRES FRANÇA LAILHACAR LEVASSEUR

val_carro = float(input("Digite o preço do carro: "))

valor_v = val_carro * 0.8
print(f"\nO preço final à vista com desconto 20% é: R$ {valor_v:.2f}")

parcelas_acrescimos = {
    6: 3,
    12: 6,
    18: 9,
    24: 12,
    30: 15,
    36: 18,
    42: 21,
    48: 24,
    54: 27,
    60: 30
}

for qtd_parcelas, acrescimo in parcelas_acrescimos.items():
    valor_acrescimo = val_carro * (1 + acrescimo / 100)
    valor_parcela = valor_acrescimo / qtd_parcelas
    print(f"O preço final parcelado em {qtd_parcelas} X é de R$ {valor_acrescimo:.2f} com parcelas de R$ {valor_parcela:.2f}")
