#Uma loja concede descontos para compras pagas com cartão de crédito e com valor superior a R$100

valor_compra = float(input("Por favor, informe o total da compra: "))

forma_pagamento = int(input("Forma de pagamento: \n 1 - Cartão de crédito \n 2 - Dinheiro \n informe a forma adotada: "))

if valor_compra > 100 and forma_pagamento == 1:
    valor_compra = valor_compra * 0.9
    print("O cliente tem direito a desconto")
    
else:
    print("O cliente não tem desconto")
 
print("O valor da compra é de {}".format(valor_compra))
#print(f"O valor da compra é de {valor_compra}")