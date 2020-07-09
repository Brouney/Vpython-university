#leibnitz
import random 
import math

plik = open('leibn.txt','a')
dlg = 106
mian = 1
minus = 1
prev = 1
tmpmian = 1
L = [1]
for i in range(1,10**7+1):
    mian +=2
    if prev == 1:
        tmpmian = mian * -1
    else:
        tmpmian = mian
    L.append(1/tmpmian)
    prev*=-1

for i in range(0,10**7):
    L[i+1] += L[i]

for i in range(0,10**7+1):
    
    if i < 100 or i == 10**3-1 or i == 10**4-1 or i == 10**5-1 or i == 10**6-1 or i == 10**7-1:
        plik.write(str(i+1)+") "+  str(4*L[i])+", "+str(4*L[i]/math.pi)+"\n")
