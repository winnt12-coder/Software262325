def d(n):
    L = []
    n = int(n)
    a = 0
    count = 0
    while(n>0):
        L.append(n % 10)
        n //= 10
    if (len(L) == 1):
        count += 1
    else:
        for i in range(len(L)-1):
            a += L[i]-L[i+1]
        if (a/(len(L)-1) == L[0]-L[1]):
            count += 1
    return count

N = int(input())
c = 0
for i in range(1,N+1):
    c += d(i)
print(c)
