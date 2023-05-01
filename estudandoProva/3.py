# Entrada de dados
numero = int(input("Digite um número de 3 dígitos: "))

# Separação dos dígitos
centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

# Inversão dos dígitos
novo_numero = unidade * 100 + dezena * 10 + centena

# Saída de dados
print("O número invertido é:", novo_numero)
