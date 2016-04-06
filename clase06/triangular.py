
while True:

    n = int(raw_input("Ingrese un N:"))
    if n <= 0:
        break

    i = 1
    while i*(i+1)/2 < n:
        i += 1

    if i*(i+1)/2 == n:
        print n, "es triangular"
    else:
        print n, "no es triangular"
