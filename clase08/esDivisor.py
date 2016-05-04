
def divisor(x, i):
    d = 1
    contador = 1
    while d < x:
        if x % d == 0:
            if contador == i:
                return d
            contador += 1
        d += 1
    return -1

"""
Para ocupar la funcion

a = int(raw_input("Ingrese un N:"))
z = int(raw_input("Ingrese el iesimo termino:"))

print divisor(a,z)
"""

def es_abundante(x):
    suma = 0
    i = 1
    while True:
        d = divisor(x, i)
        if d == -1:
            return suma > x
            """
            if suma > x:
                return True
            else:
                return False
            """
        suma += d
        i += 1


def es_abundante_2(x):
    suma = 0
    i = 1
    while divisor(x, i) != -1:
        d = divisor(x, i)
        suma += d
        i += 1

    return suma > x
    """
    if suma > x:
        return True
    else:
        return False
    """