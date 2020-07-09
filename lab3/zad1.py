
plik = open('zad1.txt','a')

for i in range (1, 101):
    for j in range (1, i+1):
        for k in range (i + 1, i + j):
            a = i * i
            b = j * j
            c = k * k
            if (a + b == c):
                plik.write(str(i) + '^2 ' + '+ ' + str(j) + '^2 ' + '= ' + str(k) + '^2' + '\n')


for i in range (1, 101):
    for j in range (1, i+1):
        for k in range (i + 1, i + j):
            a = i**3
            b = j**3
            c = k**3               
            if (a + b == c):
                plik.write(str(i) + '^3 ' + '+ ' + str(j) + '^3 ' + '= ' + str(k) + '^3' + '\n')
            
            
for i in range (1, 101):
    for j in range (1, i+1):
        for k in range (i + 1, i + j):
            a = i**4
            b = j**4
            c = k**4    
            if (a + b == c):
                plik.write(str(i) + '^4 ' + '+ ' + str(j) + '^4 ' + '= ' + str(k) + '^4' + '\n')

for i in range (1, 101):
    for j in range (1, i+1):
        for k in range (i + 1, i + j):
            a = i**5
            b = j**5
            c = k**5       
            if (a + b == c):
                plik.write(str(i) + '^5 ' + '+ ' + str(j) + '^5 ' + '= ' + str(k) + '^5' + '\n')

for i in range (1, 101):
    for j in range (1, i+1):
        for k in range (i + 1, i + j):
            a = i**6
            b = j**6
            c = k**6        
            if (a + b == c):
                plik.write(str(i) + '^6 ' + '+ ' + str(j) + '^6 ' + '= ' + str(k) + '^6' + '\n')