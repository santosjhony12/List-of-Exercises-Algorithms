i = 1
contadorIdade = 0
while i <=10:
    idade = int(input(f'Digite a idade da {i}º pessoa: '))
    i+=1
    if idade >= 18:
        contadorIdade+=1
    

print(f'Há {contadorIdade} pessoas com idade maior ou igual a 18!')