quantOtimo = 0
quantBom = 0
quantRegular = 0
quantRuim = 0
quantPessimo = 0
idadeRuim = 0
for i in range(1, 101):
    idade = int(input("\nEntre com a idade: "))
    opiniao = input("\nDigite sua opinião, sendo A = ótimo/ B = bom / C = Regular / D = Ruim/ E= pessimo: ").upper()

    if opiniao == "A":
        quantOtimo +=1
    elif opiniao == "B":
        quantBom+=1
    elif opiniao == "C":
        quantRegular+=1
    elif opiniao == "D":
        quantRuim +=1
        idadeRuim += idade
    elif opiniao == "E":
        quantPessimo+=1

diferencaPercentual = ((quantBom-quantRegular)/quantBom)*100
mediaIdadeRuim = idadeRuim/quantRuim

print("============================")
print("Quantidade de respostas ótimo: ", quantOtimo)
print("Diferença porcentual: ", diferencaPercentual)
print("Média de idade de respostas ruins: ", mediaIdadeRuim)
print()