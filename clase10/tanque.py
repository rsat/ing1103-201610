

file = open("tanque.txt", "r")

w = int(file.readline())
h = int(file.readline())
x1 = int(file.readline())
y1 = int(file.readline())
x2 = int(file.readline())
y2 = int(file.readline())

barraHorizontal = "**" * (w+2)
print barraHorizontal

for linea in range(h):
    barraHorizontalNoTrivial = "* "
    for caracter in range(w):
        if x1 == caracter and y1 == linea:
            barraHorizontalNoTrivial += "T1"
        elif x2 == caracter and y2 == linea:
            barraHorizontalNoTrivial += "T2"
        else:
            barraHorizontalNoTrivial += "  "
    print barraHorizontalNoTrivial + " *"
print barraHorizontal

# Falta encontrar error