#Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos.
#Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuario deve informar QUANTAS TRANSAÇÕES financeiras realazou ao longo de um dia
# e, na sequência, deve informar o VALOR DE CADA UMA DAS TRANSAÇÕES que realizou.
#Seu programa deverá exibir, ao final, o valor total gasto pelo usuario e tambem a media do valor de cada transação

quantidade_transacao = int(input("Informe a quantidade de transações: "))
total_transacoes = 0

for n_transacao in range(1, quantidade_transacao + 1, 1):
    transacao = float(input(f"Por favor, informe a transação de número {n_transacao}: "))
    total_transacoes = total_transacoes + transacao
    
media = total_transacoes / quantidade_transacao

print(f"Neste dia foi gasto um total de {total_transacoes} com uma média de {media} de transacao")