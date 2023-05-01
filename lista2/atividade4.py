i = 1
pessoasIdadePeso = 0
while i <=20:
    idade = int(input(f'Entre com a idade da {i} º pessoa: '))
    peso = float(input(f'Entre com a o peso da {i}º pessoa: '))
    altura = float(input(f'Entre com a altura da {i}º pessoa: '))
    olhos = input(f'Entre com a cor dos olhos da {i} º pessoa, considerando (A - Azul, P - Preto, V - Verde e C - Castanho): ')
    cabelo = input(f'Entre com a cor do cabelo da {i} º pessoa, considerando (P - Preto, C - Castanho, L - Louro e R - Ruivo): ')
    i+=1

    if idade > 50 and peso<60:
        pessoasIdadePeso += 1
    