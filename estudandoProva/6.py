prestacao = float(input("Entre com o valor da prestação: "))
acrescimo = prestacao +((prestacao/100)*10)
desconto = acrescimo - ((acrescimo/100)*10)
print("Valor a pagar: ", desconto)