#Faixa de bonús
# > 1000 3gb
# > 500 1,5gb
# > 200 500mb
# < 200 nenhum bonus

pontos = int(input("Informe a quantidade de pontos do cliente: "))
if pontos >= 1000:
    print("O cliente recebe 3gb adicionais!")
elif pontos > 500:
        print("O cliente recebe 1,5gb adicionais!")
elif pontos >= 200:
            print("O cliente recebe 200mb adicionais!")
else:
                print("O cliente não recebe dados adicionais")