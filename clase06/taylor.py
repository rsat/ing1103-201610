
while True:
    x = raw_input("Ingrese un X:")

    if x == "":
        break
    else:
        x = float(x)

    i = 0
    suma = 0
    while i < 12: # este ciclo suma el iesimo termino
        f = i
        sumaFactorial = 1.0
        while f > 0: # este ciclo calcula el factorial
            sumaFactorial *= f
            f -= 1
        suma += x**i/sumaFactorial
        i += 1
    print "el valor de e^"+str(x), suma


