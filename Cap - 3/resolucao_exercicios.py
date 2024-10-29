minutos = int(input("Informe o numero dos minutos do horario atual: "))
fatorial = minutos

for numero in range(1, minutos + 1):
    fatorial = fatorial * numero
    
print(f"A senha é LIBERDADE{fatorial}")