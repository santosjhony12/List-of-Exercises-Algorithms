deposito = float(input("\nEntre com o depósito: "))
taxa = float(input("\nEntre com a taxa de juros: "))
valor = deposito*taxa/100
total = deposito+valor
print("\nRendimentos: ",valor,"\nTotal: ",total)
print("\n")