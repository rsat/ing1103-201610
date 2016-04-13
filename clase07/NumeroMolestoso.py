def esMolestoso(n):
    if n > 999 and n < 10000:
        cuarto = n % 10
        n = n / 10
        tercero = n % 10
        n /= 10
        segundo = n % 10
        n /= 10
        primero = n
        return primero <= segundo <= tercero <= cuarto
        # if primero <= segundo <= tercero <= cuarto:
        #   return True
        # else:
        #   return False
    else:
        return False

n = int(raw_input("Ingrese un N:"))
print esMolestoso(n)