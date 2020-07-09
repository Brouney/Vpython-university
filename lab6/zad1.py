import numpy as np

def probability(x0, y0, a):
    if (a <= 85):
        x = 0.85 * x0 + 0.04 * y0
        y = -0.04 * x0 + 0.85 * y0 + 1.6
    elif (a <= 92):
        x = 0.2 * x0 - 0.26 * y0
        y = 0.23 * x0 + 0.22 * y0 + 1.6
    elif (a <= 99):
        x = -0.15 * x0 + 0.28 * y0
        y = 0.26 * x0 + 0.24 * y0 + 0.44
    else:
        x = 0
        y = 0.16 * y0

    return x, y

def function(pixels):
    X, Y = [], []
    x0, y0 = 0, 0
    p = np.random.randint(1, 101, pixels)

    for a in p:
        x, y = probability(x0, y0, a)
        X.append(x)
        Y.append(y)
        x0 = x
        y0 = y
    return X,Y


def kawalek(pixels):
    X, Y = [], []
    x0, y0 = 0,0
    i = 0
    while i < pixels:
        a = np.random.randint(1, 101)
        x, y = probability(x0, y0, a)
        if (x >= 0.8 and x <= 1.7) and (y >= 1.3 and y <= 2.0):
            X.append(x)
            Y.append(y)
            i = i + 1
        x0 = x
        y0 = y
    return X, Y


import matplotlib.pyplot as plt

plt.style.use('classic')

X, Y = function(10**6)

plt.subplot(1, 2, 1)
plt.plot(X, Y, 'r,', ms=3, zorder=1)
a = [0.8, 1.7, 1.7, 0.8, 0.8]
b = [1.3, 1.3, 2.0, 2.0, 1.3]
plt.plot(a, b, 'black')

X, Y = kawalek(10**6)
plt.subplot(1, 2, 2)
plt.plot(X, Y, 'r,', ms=3)

#plt.savefig('laboratoria.pdf',format  = 'pdf',pad_inches = 0.05)

plt.show()