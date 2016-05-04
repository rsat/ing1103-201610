

def contar_a(str):
    contador = 0
    for letra in str:
        if letra == "a":
            contador += 1
    return contador

def es_valido(email):
    if len(email) == 0:
        return False
    if email[0] == "@":
        return False
    index = email.find("@")
    return email.find(".", index+2) > 0


print es_valido("a@a.com")



