frase = str(input("Digite uma frase: ")).strip().lower()
separa = frase.split()
junta = ''.join(separa)
print(separa)

if junta == (junta[::-1]):
    print("Essa frase formam palavras palindroma")
else:
    print("Essa frase não forma palavras palindroma")