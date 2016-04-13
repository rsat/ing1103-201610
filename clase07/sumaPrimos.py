# from nombre_de_archivo import funcion
from esPrimo import esPrimo

def sumarPrimos(min, max):
    suma = 0
    for i in range(min, max + 1):
        if esPrimo(i):
            suma += i
    return suma

min = int(raw_input("Ingrese a:"))
max = int(raw_input("Ingrese b:"))
print sumarPrimos(min, max)