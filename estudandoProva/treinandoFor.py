# Lê o primeiro valor do conjunto
valor = int(input("Digite um valor (digite -1 para encerrar): "))

# Inicializa as variáveis menor e maior com o valor lido
menor = valor
maior = valor

# Executa um loop enquanto o valor lido não for -1
while valor != -1:
    # Se o valor lido for menor que a variável menor, atualiza a variável menor
    if valor < menor:
        menor = valor
    # Se o valor lido for maior que a variável maior, atualiza a variável maior
    if valor > maior:
        maior = valor
    # Lê o próximo valor do conjunto
    valor = int(input("Digite um valor (digite -1 para encerrar): "))

# Imprime o menor e o maior valor do conjunto
print("O menor valor é:", menor)
print("O maior valor é:", maior)
