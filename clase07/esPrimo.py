
# funcion que recibe un un numero natural y retorna True o False dependiendo
# si este es primo o no
def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def esPrimoConWhile(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def factorial(n):
    suma = 1
    while n > 0:
        suma *= n
        n -= 1
    return suma
