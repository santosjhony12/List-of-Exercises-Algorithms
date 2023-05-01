s = 0

for a in range(1,11):
    divisor = a/(a*a)
    if a % 2 == 0:
        s-= divisor
    else:
        s+= divisor
print(s)