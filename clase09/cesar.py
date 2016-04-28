
def cifradoCesar(x):
    abc = "abcdefghijklmnopqrstuvwxyz"
    x = x.lower()
    cifrado = ""
    for letra in x:
        if letra != " ":
            i = abc.find(letra)
            cifrado += abc[i+3 % len(abc)]
        else:
            cifrado += " "
    return cifrado

