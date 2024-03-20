def liste(n):
    liste = []
    stock = str(n)
    for i in range (len(stock)):
        liste.append(stock[i])
    return liste

a = liste(12)
print(a)

