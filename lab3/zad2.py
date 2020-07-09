import random

plik = open('zad2.txt', 'a')

plik.write(' ' * 9 + "START" + "\n")
i = 0
k = 0
while (i > -10 and i < 10):

    j = random.choice([-1, 1])
    if i > 0:
        plik.write("|" + ' ' * (10 + i) + "*" + ' ' * (10 - i) + "|+" + str(i) + "\n")
                   
    else:
        plik.write("|" + ' ' * (10 + i) + "*" + ' ' * (10 - i) + "|" + str(i) + "\n")
                  
    i += j
    k += 1

plik.write("|" + ' ' * (10 + i) + "*" + ' ' * (10 - i) + "|" + str(i) + "\n")
plik.write('Rzucono: ' + str(k) + ' razy' + '\n')
