from numpy import *
from matplotlib import pyplot


def evaluarPuntoEnPolinomio(x, coeficientes):
    suma = 0
    for i in range(len(coeficientes)):
        suma += (x**i) * coeficientes[i]
    return suma

gradoN = -1
while gradoN < 0:
    gradoN = int(raw_input("Ingrese el grado del polinomio"))


NCoeficientes = gradoN

coeficientes = []
i = 0
while NCoeficientes >= 0:
    coeficiente = int(raw_input("Ingrese el Coeficiente " + str(i)+":"))
    coeficientes.append(coeficiente)
    i += 1
    NCoeficientes -= 1

a = int(raw_input("Ingrese a:"))
b = a - 1
while b < a:
    b = int(raw_input("Ingrese b:"))

X = linspace(a,b,1000)
Y = []

print
for x in X:
    Y.append(evaluarPuntoEnPolinomio(x, coeficientes))

pyplot.plot(X,Y)
pyplot.show()