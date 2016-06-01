
from numpy import *
from matplotlib import pyplot

X1 = []
for x1 in range(1000):
    X1.append(random.randint(0,10))

d1 = {}
for x1 in X1:
    if x1 in d1:
        d1[x1] += 1
    else:
        d1[x1] = 1


X2 = []
for x2 in range(10000):
    X2.append(random.randint(0,100))

d2 = {}
for x2 in X2:
    if x2 in d2:
        d2[x2] += 1
    else:
        d2[x2] = 1

X3 = []
for x3 in range(100000):
    X3.append(random.randint(0,1000))

d3 = {}
for x3 in X3:
    if x3 in d3:
        d3[x3] += 1
    else:
        d3[x3] = 1

"""
pyplot.plot(range(0,10), d1.values())
pyplot.plot(range(0,100), d2.values())
pyplot.plot(range(0,1000), d3.values())
"""

fig = pyplot.subplot(3, 1, 1)
fig.plot(range(0,10), d1.values(), 'b')

fig = pyplot.subplot(3, 1, 2)
fig.plot(range(0,100), d2.values(), 'r')

fig = pyplot.subplot(3, 1, 3)
fig.plot(range(0,1000), d3.values(), 'g')


pyplot.show()