def contarPalabras(frase):
    d = {}
    for palabra in frase.split(' '):
        if len(palabra) > 3:
            if palabra not in d:
                d[palabra] = 1
            else:
                d[palabra] += 1
    return d


def transformarATuplas(frase):
    tuplas = []
    d = contarPalabras(frase)

    for llave in d:
        tuplas.append((llave, d[llave]))
    return tuplas


print transformarATuplas("El curso de introduccion a la programacion es un curso donde tenemos varias evaluaciones")