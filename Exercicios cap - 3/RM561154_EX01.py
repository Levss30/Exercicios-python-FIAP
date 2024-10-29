#RM561154
#NOME: LUCAS ANDRES FRANÇA LAILHACAR LEVASSEUR

voto_1 = input("Informe o melhor dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA \n") 
voto_2 = input("Informe o melhor dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA \n") 
voto_3 = input("Informe o melhor dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA \n") 
voto_4 = input("Informe o melhor dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA \n") 
voto_5 = input("Informe o melhor dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA \n") 
voto_6 = input("Informe o melhor dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA \n") 
voto_7 = input("Informe o melhor dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA \n")

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

if voto_1.upper() == "SEGUNDA-FEIRA" or "SEGUNDA":
    segunda = segunda + 1
elif voto_1.upper() == "TERÇA-FEIRA" or "TERÇA":
    terca = terca + 1
elif voto_1.upper() == "QUARTA-FEIRA" or "QUARTA":
    quarta = quarta + 1
elif voto_1.upper() == "QUINTA-FEIRA" or "QUINTA":
    quinta = quinta + 1
elif voto_1.upper() == "SEXTA-FEIRA" or "SEXTA":
    sexta = sexta + 1
else:
    print("O colaborador 1 digitou um console inexistente e seu voto será desconsiderado")
    
if voto_2.upper() == "SEGUNDA-FEIRA" or "SEGUNDA":
    segunda = segunda + 1
elif voto_2.upper() == "TERÇA-FEIRA" or "TERÇA":
    terca = terca + 1
elif voto_2.upper() == "QUARTA-FEIRA" or "QUARTA":
    quarta = quarta + 1
elif voto_2.upper() == "QUINTA-FEIRA" or "QUINTA":
    quinta = quinta + 1
elif voto_2.upper() == "SEXTA-FEIRA" or "SEXTA":
    sexta = sexta + 1
else:
    print("O colaborador 2 digitou um console inexistente e seu voto será desconsiderado")

if voto_3.upper() == "SEGUNDA-FEIRA" or "SEGUNDA":
    segunda = segunda + 1
elif voto_3.upper() == "TERÇA-FEIRA" or "TERÇA":
    terca = terca + 1
elif voto_3.upper() == "QUARTA-FEIRA" or "QUARTA":
    quarta = quarta + 1
elif voto_3.upper() == "QUINTA-FEIRA" or "QUINTA":
    quinta = quinta + 1
elif voto_3.upper() == "SEXTA-FEIRA" or "SEXTA":
    sexta = sexta + 1
else:
    print("O colaborador 3 digitou um console inexistente e seu voto será desconsiderado")
    
if voto_4.upper() == "SEGUNDA-FEIRA" or "SEGUNDA":
    segunda = segunda + 1
elif voto_4.upper() == "TERÇA-FEIRA" or "TERÇA":
    terca = terca + 1
elif voto_4.upper() == "QUARTA-FEIRA" or "QUARTA":
    quarta = quarta + 1
elif voto_4.upper() == "QUINTA-FEIRA" or "QUINTA":
    quinta = quinta + 1
elif voto_4.upper() == "SEXTA-FEIRA" or "SEXTA":
    sexta = sexta + 1
else:
    print("O colaborador 4 digitou um console inexistente e seu voto será desconsiderado")
    
if voto_5.upper() == "SEGUNDA-FEIRA" or "SEGUNDA":
    segunda = segunda + 1
elif voto_5.upper() == "TERÇA-FEIRA" or "TERÇA":
    terca = terca + 1
elif voto_5.upper() == "QUARTA-FEIRA" or "QUARTA":
    quarta = quarta + 1
elif voto_5.upper() == "QUINTA-FEIRA" or "QUINTA":
    quinta = quinta + 1
elif voto_5.upper() == "SEXTA-FEIRA" or "SEXTA":
    sexta = sexta + 1
else:
    print("O colaborador 5 digitou um console inexistente e seu voto será desconsiderado")
    
if voto_6.upper() == "SEGUNDA-FEIRA" or "SEGUNDA":
    segunda = segunda + 1
elif voto_6.upper() == "TERÇA-FEIRA" or "TERÇA":
    terca = terca + 1
elif voto_6.upper() == "QUARTA-FEIRA" or "QUARTA":
    quarta = quarta + 1
elif voto_6.upper() == "QUINTA-FEIRA" or "QUINTA":
    quinta = quinta + 1
elif voto_6.upper() == "SEXTA-FEIRA" or "SEXTA":
    sexta = sexta + 1
else:
    print("O colaborador 6 digitou um console inexistente e seu voto será desconsiderado")
    
if voto_7.upper() == "SEGUNDA-FEIRA" or "SEGUNDA":
    segunda = segunda + 1
elif voto_7.upper() == "TERÇA-FEIRA" or "TERÇA":
    terca = terca + 1
elif voto_7.upper() == "QUARTA-FEIRA" or "QUARTA":
    quarta = quarta + 1
elif voto_7.upper() == "QUINTA-FEIRA" or "QUINTA":
    quinta = quinta + 1
elif voto_7.upper() == "SEXTA-FEIRA" or "SEXTA":
    sexta = sexta + 1
else:
    print("O colaborador 7 digitou um console inexistente e seu voto será desconsiderado")
    
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia escolhido pelos colaboradores é: Segunda-feira")
    
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia escolhido pelos colaboradores é: Terça-feira")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia escolhido pelos colaboradores é: Quarta-feira")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O dia escolhido pelos colaboradores é: Quinta-feira")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("O dia escolhido pelos colaboradores é: Sexta-feira")
else:
    print("Houve empate, por favor entrar em contato com a direção")
