#o algoritimo da sorte de Fibonnaci.
#A ideia dessa empresa, é claro, é fazer com que seja mais dificil os jogadores terem sucesso nas ações que realizam nos games.
# Por isso o seu algoritmo deverá funcionar da seguinte forma: o usuario deve digitar um valor numérico inteiro e o algoritmo deverá
#verificar se esse valor encontra-se na sequência de Fibonnaci. Caso o número esteja na sequência, o algoritmo deve exibir a mensagem "Ação bem sucedida!"
#caso não esteja, deve exibir a mensagem "A ação falhou...".

#A sequência de Fibonnaci é muito simples e possui uma lógica de facil compreensão: ela se inicia em 1 e cada novo elemento da sequência é a soma entre os dois eleentos anteriores.
# Portanto: 1, 1, 2, 3, 5, 8, 13, 21, e assim por diante.
#Logo, se o usuario digitar o numero 55 o programa deverá informar que a ação foi bem sucedida, afinal 55 está entre os número da sequência
#Mas se o usuario digitar o numero 6, por exemplo, a ação não será bem sucedida, pois o numero 6 não está na sequencia.

numero_usuario = int(input("Por favor, informe um número inteiro: "))
anterior_1 = 1
anterior_2 = 0

for n_elemento in range(1, numero_usuario + 1, 1):
    v_atual = anterior_1 + anterior_2
    anterior_1 = anterior_2
    anterior_2 = v_atual
    if numero_usuario == v_atual:
        print("Ação bem sucedida!")
        break
    elif numero_usuario < v_atual:
        print("A ação falhou...")
        break