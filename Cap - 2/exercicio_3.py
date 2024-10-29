#Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganharem um console de última geração cada um por conta do bom desempenho que tiveram nos ultimos projetos.
# Por uma questão de logistica, porém, a empresa pede que todos os 5 membros da equipe recebam o mesmo aparelho.
# Crie um algoritimo onde o usuario possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.

#As opções são: PLAYSTATION, XBOX, NINTENDO

voto_1 = input("Informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO \n") 
voto_2 = input("Informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO \n") 
voto_3 = input("Informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO \n") 
voto_4 = input("Informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO \n") 
voto_5 = input("Informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO \n") 

playstation = 0
xbox = 0
nintendo = 0

if voto_1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_1.upper() == "XBOX":
    xbox = xbox + 1
elif voto_1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 1 digitou um console inexistente e seu voto será desconsiderado")

if voto_2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_2.upper() == "XBOX":
    xbox = xbox + 1
elif voto_2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 2 digitou um console inexistente e seu voto será desconsiderado")

if voto_3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_3.upper() == "XBOX":
    xbox = xbox + 1
elif voto_3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 3 digitou um console inexistente e seu voto será desconsiderado")

if voto_4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_4.upper() == "XBOX":
    xbox = xbox + 1
elif voto_4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 4 digitou um console inexistente e seu voto será desconsiderado")

if voto_5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_5.upper() == "XBOX":
    xbox = xbox + 1
elif voto_5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 5 digitou um console inexistente e seu voto será desconsiderado")
    
if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi o Playstation")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o Xbox")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi o Nintendo")
else:
    print("Houve empate, por favor entrar em contato com a direção")
