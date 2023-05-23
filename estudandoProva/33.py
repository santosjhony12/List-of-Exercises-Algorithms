totalNascidos = int(input("\nEntre com o total de crianças nascidas no período: "))
sexoCrianca = ""
quantRecemNascidos = 0
quantMeninos = 0
quantMeninas = 0
quantDias = 0
maiorNumeroDias = 0

while sexoCrianca != "X":
    sexoCrianca = input("\nEntre com o sexo do recém-nascidos prematuros, sendo M - masculino, F - feminino e X - para sair: ").upper()

    if sexoCrianca == "X":
        break
    quantRecemNascidos +=1 
    numeroDias = int(input("\nEntre com a quantidade de dias que foi mantido na enculbadora: "))

    #valor que acumulara o total de dias para tirar a média
    quantDias = quantDias + numeroDias

    if maiorNumeroDias<numeroDias:
        maiorNumeroDias = numeroDias

    if sexoCrianca == "M":
        quantMeninos +=1
    elif sexoCrianca == "F":
        quantMeninas += 1


porcentagemPrematuros = (quantRecemNascidos*100)/totalNascidos
porcentagemMeninosPrematuros = (quantMeninos*100)/quantRecemNascidos
porcentagemMeninasPrematuras = (quantMeninas*100)/quantRecemNascidos
mediaDias = quantDias/quantRecemNascidos
print("=====================================")
print("Porcentagem de prematuros: ", porcentagemPrematuros,"%")
print("Porcentagem de meninos prematuros: ", porcentagemMeninosPrematuros,"%")
print("Porcentagem de meninas prematuras: ", porcentagemMeninasPrematuras,"%")
print("Média de dias de crianças recém nascidas prematuras: ", mediaDias)
print("Maior número de dias de uma criança na encubadora: ", maiorNumeroDias)
print("=====================================")