nome1 = input("Entre com o nome do país 1: ")
ouro1 = int(input("Entre com a quantidade de medalhas de ouro do país 1: "))
prata1 = int(input("Entre com quantidade de medalhas de prata do pái 1: "))
bronze1 = int(input("Entre com a quantidade de medalhas de bronze do país1: "))

nome2 = input("Entre com o nome do país 2: ")
ouro2 = int(input("Entre com a quantidade de medalhas de ouro do país 2: "))
prata2 = int(input("Entre com quantidade de medalhas de prata do pái 2: "))
bronze2 = int(input("Entre com a quantidade de medalhas de bronze do país 2: "))



nome3 = input("Entre com o nome do país 3: ")
ouro3 = int(input("Entre com a quantidade de medalhas de ouro do país 3: "))
prata3 = int(input("Entre com quantidade de medalhas de prata do pái 3: "))
bronze3 = int(input("Entre com a quantidade de medalhas de bronze do país 3: "))

total1 = ouro1*3+prata1*2+bronze1*1
total2 = ouro2*3+prata2*2+bronze2*1
total3 = ouro3*3+prata3*2+bronze3*1

if total1>total2:
    if total1>total3:
        if total2>total3:
            print("1º lugar: ", nome1)
            print("2º lugar: ", nome2)
            print("3º lugar: ", nome3)
        else:
            print("1º lugar: ", nome1)
            print("2º lugar: ", nome3)
            print("3º lugar: ", nome2)
    elif total3>total2:
        print("1º lugar: ", nome1)
        print("2º lugar: ", nome3)
        print("3º lugar: ", nome2)
