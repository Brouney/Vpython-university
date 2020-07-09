import numpy as np

def Silnia(licznik: int):
    if (licznik == 0):
            return 1
    if (licznik == 1):
            return np.sqrt(np.pi) / 2
    elif (licznik%2 == 0):
            return licznik / 2 * Silnia (licznik - 2)
    else:
            return licznik / 2. * Silnia (licznik - 2)

