pal = input("\nDigite a palavra: ")
letra = pal[0]

if (letra == "l" or letra == "L" or letra == "d" or letra =="D"):
    pal1 = pal[0] + pal[1]
    pal2 = pal[-1]
    pal1 = pal1+pal2
    #o exercicio não pede para imprimir na tela do usuário o resultado, mas print(pal1)
else:
    pal1 = pal[1:]
    print("\nPalavra: ",pal1)
print("\n")