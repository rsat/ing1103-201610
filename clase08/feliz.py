def sumaDigitosCuadrados(x):
    suma = 0
    while x > 0:
        d = x % 10
        suma += d**2
        x /= 10
    return suma

def esFeliz(x):
    while True:
        sumaDigitos = sumaDigitosCuadrados(x)
        if sumaDigitos == 1:
            return True
        if sumaDigitos == 4 or sumaDigitos == 16 or sumaDigitos == 37 or \
            sumaDigitos == 58 or sumaDigitos == 89 or sumaDigitos == 145 or \
            sumaDigitos == 42 or sumaDigitos == 20:
            return False
        x = sumaDigitos

print esFeliz(19)