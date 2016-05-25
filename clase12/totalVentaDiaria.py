
monedas = {'USD' : ('Dolares', 500),
          'EUR' : ('Euros', 600),
          'GBP' : ('Libras', 700),
          'CLP' : ('Pesos Chilenos', 1)}


ventaDiaria = [('USD', 50), ('GBP', 200), ('EUR', 300),
               ('GBP', 100), ('CLP', 21000), ('USD', 150),
               ('EUR', 100)]


def porMoneda(monedas, ventaDiaria):
    d = {}
    for venta in ventaDiaria:
        descripcionMoneda = monedas[venta[0]][0]
        if descripcionMoneda in d:
            d[descripcionMoneda] += venta[1]
        else:
            d[descripcionMoneda] = venta[1]
    return d

print porMoneda(monedas, ventaDiaria)


def totalVentaDiaria(monedas, ventaDiaria):
    suma = 0
    ventaAcumuladas = porMoneda(monedas, ventaDiaria)
    for ventaAcumulada in ventaAcumuladas:
        for moneda in monedas.values():
            if moneda[0] == ventaAcumulada:
                suma += ventaAcumuladas[ventaAcumulada] * moneda[1]
    return suma

print totalVentaDiaria(monedas, ventaDiaria)