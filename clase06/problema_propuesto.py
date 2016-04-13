# -*- coding: utf-8 -*-
"""
Escriba un programa que pida un entero positivo al usuario y lo aproxime a la decena más cercana.

Ejemplos:
2     --> 0 
5     --> 10 
12    --> 10
15    --> 20 
150   --> 150 
175   --> 180
1212  --> 1210
1795  --> 1800
30001 --> 30000
99999 --> 100000

"""

numeroEntero = int(raw_input("Ingrese numero a redondear: "))
while numeroEntero % 10 != 0:
    if numeroEntero % 10 >= 5:
        numeroEntero += 1
    else:
        numeroEntero -= 1
print numeroEntero


# otra opción sin utilizar while
numeroEntero = int(raw_input("Ingrese numero a redondear: "))
print 10 * ((numeroEntero + 5) // 10)
