diaAni = int(input("Digite o dia de seu aniversario: "))
mesAni = int(input("Digite o mes de seu aniversario: "))
anoAni = int(input("Digite o ano de seu aniversario: "))
diaAtual = int(input("Digite o dia atual: "))
mesAtual = int(input("Digite o mes atual: "))
anoAtual = int(input("Digite o ano atual: "))

anoIdade = anoAtual-anoAni
diaIdade = anoIdade*365
mesIdade = anoIdade*12
print("Anos: ", anoIdade)
print("Dias: ", diaIdade)
print("Meses: ", mesIdade)