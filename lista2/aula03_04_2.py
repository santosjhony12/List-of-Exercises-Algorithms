litros = float(input("Entre com a quant. de litros vendidos: "))
tipo = input("Entre com o tipo de combustível (A - Alcool / G - Gasolina): ")

valor_litro = 3.3

if (tipo == 'A'):
    if (litros <= 20):
        total = valor_litro*litros-((valor_litro*litros)*0.3)
        print ("Valor a ser pago: ",total)
    elif(litros > 20):
        total = valor_litro*litros-((valor_litro*litros)*0.5)
        print ("Valor a ser pago: ",total)
elif (tipo =='G'):
    if(litros <= 20):
        total = valor_litro*litros-((valor_litro*litros)*0.4)
        print ("Valor a ser pago: ",total)
    elif(litros > 20):
        total = valor_litro*litros-((valor_litro*litros)*0.6)
        print ("Valor a ser pago: ",total)
else:
    print("Entrada de dados incorreta")