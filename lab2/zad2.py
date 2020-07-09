import random
import math
plik = open('zad2.txt','a')
strzelone = 0
for i in range(1,10**6+1):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <=1:
        strzelone +=1
    if i <= 100 or i == 10**3 or i == 10**4 or i == 10**5 or i == 10**6 :
        plik.write(str(i)+") "+str(4 * strzelone /i)+", "+str(4 * strzelone /i/math.pi)+"\n")
