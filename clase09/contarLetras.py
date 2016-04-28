

frase = raw_input("Ingrese una frase:")

abc = "abcdefghijklmnopqrstuvwxyz"
frase = frase.lower()
for letra in abc:
    ocurrencias = frase.count(letra)
    if ocurrencias > 0:
        print letra + ":", ocurrencias

