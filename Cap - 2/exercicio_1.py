# Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar que o usuário informe
# o seu número de BATIMENTOS POR MINUTO (BPM) e IDADE. A partir disso o script deva verificar e exibir uma mensagem informando se os 
# batimentos do usuario encontram-se DENTRO da faixa adequada, de acordo com o site Tua Saude

# IDADE BPM
# Até 2 anos 120 a 140
# De 8 até 17 anos 80 a 100
# Adulto sedentário 70 a 80 
# Idoso 50 a 60

print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")

idade = int(input("Por favorm, informe a sua idade: "))
bpm = int(input("Por favor, informe a sua frequência cardiaca: "))

if idade < 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequência cardiaca adequada")
    else:
        print("frequência cardiaca inadequada")
elif idade > 8 and idade <= 17:
    if bpm >= 120 and bpm <= 100:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")
        
elif idade > 18 and idade <= 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")
        
elif idade > 60:
    if bpm >= 50 and bpm <= 60:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")

else:
    print("Não existem dados para a idade adequada")
# if idade <= 2:
#     if bpm >= 120:
#         if bpm <= 140:
#             print("Batimentos normais para a idade fornecida")
#         else:
#             print("Batimentos acima dos indicados a idade")
#     else:
#         print("Batimentos abaixo dos indicados a idade")
# elif idade >= 8:
#         if idade <= 17:
#             if bpm >= 80:
#                 if bpm <= 100:
#                     print("Batimentos normais para a idade fornecida")
#                 else:
#                     print("Batimentos acima para a idade fornecida")
#             else:
#                 print("Batimentos abaixo para a idade fornecida")
# elif idade >= 18:
#     if idade <= 60:
#         if bpm > 70:
#             if bpm <= 80:
#                 print("Batimentos normais para a idade fornecida")
#             else:
#                 print("Batimentos acima para a idade fornecida")
#         else:
#             print("Batimentos abaixo para a idade fornecida")
#     else: 
#         if bpm >= 50:
#             if bpm <= 60:
#                 print("Batimentos normais para a idade")
#             else:
#                 print("Batimentos acima para a idade fornecida")
#         else:
#             print("Batimentos abaixo para a idade fornecida")
# else:
#     print("Não foi possivel verificar os batimentos para essa idade")
        