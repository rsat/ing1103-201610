

monedas = {'USD' : ('Dolares', 500),
          'EUR' : ('Euros', 600),
          'GBP' : ('Libras', 700),
          'CLP' : ('Pesos Chilenos', 1)}


ventaDiaria = [('USD', 50), ('GBP', 200), ('EUR', 300),
               ('GBP', 100), ('CLP', 21000), ('USD', 150),
               ('EUR', 100)]


def porMoneda2(ventaDiaria):
    d = {}
    for venta in ventaDiaria:
        if venta[0] in d:
            d[venta[0]] += venta[1]
        else:
            d[venta[0]] = venta[1]
    return d

print porMoneda2(ventaDiaria)

def porMoneda(monedas, ventaDiaria):
    d = {}
    for venta in ventaDiaria:
        descripcionMoneda = monedas[venta[0]][0]
        if descripcionMoneda in d:
            d[descripcionMoneda] += venta[1]
        else:
            d[descripcionMoneda] = venta[1]
    return d

#print porMoneda(monedas, ventaDiaria)