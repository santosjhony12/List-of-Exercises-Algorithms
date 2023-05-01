altura = float(input("Digite sua altura: "))
sexo = input("Digite o sexo (M - masculino / F - Feminino: )")

print(sexo)
if (sexo=='M'):
    peso_ideal = (72.7*altura)-58
    print(f'Peso ideal: {peso_ideal}')
elif (sexo=='F'):
    peso_ideal = (62.1*altura)-44.7
    print(f'Peso ideal: {peso_ideal}')
else:
    print("Sua opção é invalida")