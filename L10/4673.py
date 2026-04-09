def d(n):
    n = int(n)
    N = n
    while(n > 0):
        N += n%10
        n //= 10
    return N
L = []
for i in range(1, 10001):
    L.append(d(i))

for i in range(1, 10001):
    if i not in L:
        print(i)
