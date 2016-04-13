from esPrimo import factorial

while True:
    x = raw_input("Ingrese un X:")

    if x == "":
        break
    else:
        x = float(x)

    i = 0
    suma = 0
    while i < 12: # este ciclo suma el iesimo termino
        suma += x**i/factorial(i)
        i += 1
    print "el valor de e^"+str(x), suma