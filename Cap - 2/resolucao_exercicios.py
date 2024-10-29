faturamento_anual = float(input("Por favor, informe seu faturamento anual: "))
tipo_assinatura =  input("Por favor, informe o seu tipo de assinatura: \n Basic \n Silver \n Gold \n Platinum \n ")


if tipo_assinatura.upper() == "BASIC":
    bonus = faturamento_anual * 0.3
elif tipo_assinatura.upper() == "SILVER":
    bonus = faturamento_anual * 0.2
elif tipo_assinatura.upper() == "GOLD":
    bonus = faturamento_anual * 0.1
elif tipo_assinatura.upper() == "PLATINUM":
    bonus = faturamento_anual * 0.5
else:
    bonus = 0
    print("Tipo de assinatura invalida!")
    
print(f"Para um faturamento anual de {faturamento_anual} o bonus é de {bonus} ")