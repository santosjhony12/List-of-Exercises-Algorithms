indice = float(input("\nDigite o indice de poluição: "))
if (indice>= 0.5):
    print("\nSuspender as atividades das industrias 1, 2 e 3 ")
elif(indice>=0.4):
    print("\nSuspender as atividades das industrias 1 e 2")
elif (indice>=0.3):
    print("\nSuspender as atividades da industria 1")
else:
    print("\nIndice de poluição aceitavel em todos os grupos")
print("\n")