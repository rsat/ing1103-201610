# Programa que pide un N, e imprime los números primos naturales menores iguales a N

N = int(raw_input("Ingrese un N:"))

i = 2
while i <= N:
    x = 2
    esPrimo = True
    while x < i:
        if i % x == 0:
            esPrimo = False
            break
        x += 1

    if esPrimo:
        print i

    i += 1