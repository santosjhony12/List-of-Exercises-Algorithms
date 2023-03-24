num = float(input("\nEntre com um numero com parte fracionária: "))
numi = float(int(num-0.5))
numfrac = num - numi
numa = float(int(num+0.00001))
print("\nParte inteira: ", numi)
print("\nParte fracionada: ", round((numfrac+0.00001),3))
print("\nNúmero arrendondado: ", numa)
print("\n")