
def esPalindroma(x):
    i = 0
    j = len(x) - 1
    while i < j:
        while x[i] == " " and i < len(x)-1:
            i += 1
        while x[j] == " " and j > 0:
            j -= 1
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True


print esPalindroma("    ")