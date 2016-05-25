
def contarPalabras(frase):
    d = {}
    for palabra in frase.split(' '):
        if len(palabra) > 3:
            if palabra not in d:
                d[palabra] = 1
            else:
                d[palabra] += 1
    return d


print contarPalabras("El curso de introduccion a la programacion es un curso donde tenemos varias evaluaciones")