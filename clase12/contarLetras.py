


def contarLetras(palabra):
    d = {}
    for letra in palabra:
        if letra != ' ':
            if letra not in d:
                d[letra] = 1
            else:
                d[letra] += 1
    return d

d = contarLetras('cualquiercosa')
letras = d.keys()
letras.sort(reverse=True)
for letra in letras:
    print letra,":",d[letra]