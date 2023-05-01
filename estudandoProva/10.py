idade = int(input("Digite a sua idade: "))

if idade<16:
    print("Não votante")
elif idade>= 18 and idade<=65:
    print("Voto obrigatorio")
elif idade>=16 and idade<18:
    print("Voto opcional")
elif idade>65: 
    print("Voto facultativo")