import numpy as np
import zad1

wymiary = np.zeros (18)
tab = np.random.uniform(-1, 1, (10**6, 18)) ** 2

for i in range(0, 10**6):
    for j in range(2, 18):
        if (np.sum (tab[i,0:j]) > 1):
            break
        else:
            wymiary[j - 1] += 1

plik = open('potegi.txt', 'w')

for k in range(1, 18):
    Vmat = (np.power(np.pi, ((k + 1)/ 2.))) / zad1.Silnia(k + 1)
    Vwyl = np.power(2, k + 1) * (wymiary[k] / 10**6)
    plik.write (str (k + 1) + ') ' + str(Vwyl) + '  ' + str(Vmat) + '  ' + str(Vwyl/Vmat) + '  '+ str(wymiary[k]) + '\n')

plik.close()