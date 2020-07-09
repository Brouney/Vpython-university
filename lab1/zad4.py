inputted = int(input("Prosze podać liczbe: "))

dzielnik = int(inputted/2)
if inputted == 0:
    print("liczba parzysta")

for licz in range(2,dzielnik):
    if inputted % licz == 0:
        break
else:
    print("liczba jest pierwsza")
        

if inputted %2 ==0:
    print("liczba parzysta")
else:
    print("liczba nieparzysta")
