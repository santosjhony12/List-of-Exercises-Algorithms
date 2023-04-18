peso = float(input("\nDigite o peso: "))
idade = int(input("\nDigite a idade: "))
gotas = 500/20  # calculo do numero de mg por gotas 
if (peso <5) :
    print("\nNão pode tomar o remedio porque não tem peso. Consulte o médico. ")
else:
    if(idade>=12):
        if (peso>=60):
            print("\nTomar ", 1000/gotas," gotas")
        else:
            print("\nTomar ",875/gotas, " gotas")
    else: 
        if (peso<=9):
            print("\nTomar ",125/gotas," gotas")
        elif(peso<=16):
            print("\nTomar ", 250/gotas, " gotas")
        elif(peso<=24):
            print("\nTomar ", 375/gotas, " gotas")
        elif (peso<=30):
            print("\nTomar ", 500/gotas, " gotas")
        else: 
            print("\nTomar ", 750/gotas, " gotas")
print("\n")