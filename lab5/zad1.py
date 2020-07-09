import numpy as np
import matplotlib.pyplot as plt

a = np.arange(1,367,1)
#print(sum(a==2))
file = open("zad1wyn.txt","w")
tab2 = []
tab3 = []
tab4 = []
for N in range(1,367):
    liczba2 = 0
    liczba3=0
    liczba4=0
    temp = np.zeros((1000,367))
    for t in range(1000):

        for i in range(N):
            day = np.random.randint(1,367)
            temp[t][day]+=1

    for z in range(1000):
        if sum(temp[z]>=2) > 0:
            liczba2+=1
        if sum(temp[z]>=3) > 0:
            liczba3+=1
        if sum(temp[z]>=4) > 0:
            liczba4+=1
    file.write(str(N)+") "+str(liczba2/1000)+"\n")
    tab2.append(liczba2/1000)
    tab3.append(liczba3/1000)
    tab4.append(liczba4/1000)

plt.rcParams['font.size']=18
plt.rcParams['legend.fontsize']=18
plt.plot(a,tab2,'-',label = 'wieksze od 2')
#plt.savefig('myfig2.pdf',format='pdf')
#plt.show

plt.plot(a,tab3,'-',label = 'wieksze od 3')
#plt.savefig('myfig3.pdf',format='pdf')
#plt.show

plt.plot(a,tab4,'-',label = 'wieksze od 4')
plt.legend(loc='upper right')
plt.savefig('myfig.pdf',format='pdf')
plt.show