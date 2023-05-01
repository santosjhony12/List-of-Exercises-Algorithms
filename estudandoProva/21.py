voto = int(input("Digite o seu voto: "))
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
votoNulo = 0
votoBranco = 0
total = 0

while voto!= 0:
    if(voto==1):
        cand1 +=1
    elif (voto==2):
        cand2+=1
    elif(voto==3):
        cand3+=1
    elif(voto==4):
        cand4 +=1
    elif(voto==5):
        votoNulo+=1
    elif(voto==6):
        votoBranco+=1
    else: 
        print("Digite um valor valido")
    total+=1
    voto = int(input("Digite o seu voto: "))

print("TOTAL DE VOTOS / PERCENTUAL SOBRE O TOTAL")
print("Cand1 = ", cand1, " / ", ((cand1/total)*100), "%")
print("Cand2 = ", cand2, " / ", ((cand2/total)*100), "%")
print("Cand3 = ", cand3, " / ", ((cand3/total)*100), "%")
print("Cand4 = ", cand4, " / ", ((cand4/total)*100), "%")
print("Voto Nulo = ", votoNulo, " / ", ((votoNulo/total)*100), "%")
print("Voto em Branco = ", votoBranco, " / ", ((votoBranco/total)*100), "%")