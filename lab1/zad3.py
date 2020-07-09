max = 10000
def generujliczby():
    
    doskonale = []
    for i in range(1,max):
        sum =0

        for t in range(1,(i//2)+1):
            if i % t == 0:
                sum += t
        if sum == i:
            doskonale.append(i)

    return doskonale

print (generujliczby())
