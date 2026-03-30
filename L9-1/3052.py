L = []
for i in range(10):
    N = int(input())
    N = N%42
    if (N not in L):
        L.append(N)
print(len(L))
