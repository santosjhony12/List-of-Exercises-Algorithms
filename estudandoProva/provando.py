# Solicita o valor atual do salário mínimo ao usuário
salario_minimo = float(input("Digite o valor atual do salário mínimo: "))

# Loop para ler os dados de cada contribuinte
for i in range(10):
    cpf = input("Digite o CPF do contribuinte: ")
    dependentes = int(input("Digite o número de dependentes: "))
    renda_mensal = float(input("Digite a renda mensal: "))

    # Calcula o valor do desconto para os dependentes
    desconto_dependentes = (5/4) * salario_minimo * dependentes

    # Calcula a renda líquida do contribuinte (com o desconto dos dependentes)
    renda_liquida = renda_mensal - desconto_dependentes

    # Define a alíquota de acordo com a renda líquida
    if renda_liquida <= 2 * salario_minimo:
        aliquota = 0
    elif renda_liquida <= 3 * salario_minimo:
        aliquota = 0.05
    elif renda_liquida <= 5 * salario_minimo:
        aliquota = 0.1
    elif renda_liquida <= 7 * salario_minimo:
        aliquota = 0.15
    else:
        aliquota = 0.2

    # Calcula o valor do imposto de renda a ser pago
    imposto_renda = renda_liquida * aliquota

    # Imprime os resultados para o contribuinte atual
    print("CPF: ", cpf)
    print("Dependentes: ", dependentes)
    print("Renda mensal: R$", renda_mensal)
    print("Desconto dos dependentes: R$", desconto_dependentes)
    print("Renda líquida: R$", renda_liquida)
    print("Alíquota: ", aliquota*100, "%")
    print("Imposto de renda a pagar: R$", imposto_renda)
    print("-------------------------------------------")
