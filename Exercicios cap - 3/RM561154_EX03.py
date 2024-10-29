#RM561154
#NOME: LUCAS ANDRES FRANÇA LAILHACAR LEVASSEUR

valor_divida = float(input("Digite o valor da dívida: "))

parcelas_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}


for qtd_parcelas, percentual_juros in parcelas_juros.items():
    valor_juros = valor_divida * (percentual_juros / 100)
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / qtd_parcelas
    print(f"Total: R$ {valor_total:.2f} Juros: R$ {valor_juros:.2f} Número de parcelas: {qtd_parcelas} Valor da Parcela: R$ {valor_parcela:.2f}")
