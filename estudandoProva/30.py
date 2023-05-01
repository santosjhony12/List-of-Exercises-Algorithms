salarioMinimo = 1300.00
for i in range(1, 11):
    cpf = input("\nDigite o CPF: ")
    dependentes = int(input("\nDigite o número de dependentes, caso não tenha, digite 0: "))
    rendaMensal = float(input("\nDigite o valor do salário: "))

    desconto = rendaMensal - (rendaMensal*((5*dependentes)/100))

    if rendaMensal>(salarioMinimo*7):
        valorPagar = desconto*0.2
    elif rendaMensal>(salarioMinimo*5):
        valorPagar = desconto*0.15
    elif rendaMensal>(salarioMinimo*3):
        valorPagar = desconto*0.10
    elif rendaMensal>(salarioMinimo*2):
        valorPagar = desconto*0.05
    else:
        valorPagar = "Insento"
    print("\nO valor a ser pago é: ", valorPagar)