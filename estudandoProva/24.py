maiorAltura = 0
menorAltura = 0
controler = False
alturaF = 0
controlerF = 0
controlerM = 0

for pessoa in range(1, 51):
    alturaEntrada = float(input("Digite a altura: "))
    sexoEntrada = input("Digite o sexo(M - masculino e F - Feminino: )").upper()
    
    if controler == False:
        controler = True
        menorAltura = alturaEntrada

    if maiorAltura<alturaEntrada:
        maiorAltura = alturaEntrada
    elif menorAltura>alturaEntrada:
        menorAltura = alturaEntrada

    if sexoEntrada == "F":
        alturaF +=alturaEntrada
        controlerF +=1
    elif sexoEntrada == "M":
        controlerM +=1
    else:
        print("O sexo informado não é válido")
        
diferenca =(controlerM-controlerF)/controlerF*100

print(f'Maior altura {maiorAltura}\nMenor Altura: {menorAltura}\nMédia de altura de mulheres: {(alturaF/controlerF)}\nQuantidade de homens: {controlerM}\nDiferença: {diferenca}%')
