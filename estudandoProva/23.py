# Solicita ao usuário os valores de N1 e N2
n1 = int(input("Digite o valor de N1: "))
n2 = int(input("Digite o valor de N2: "))

# Loop para percorrer todos os números entre N1 e N2
for num in range(n1, n2+1):

    # Verifica se o número é primo
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Se o número for primo, imprime-o
    if is_prime and num > 1:
        print(num)

