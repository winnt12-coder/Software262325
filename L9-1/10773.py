N = int(input())
L = []

for i in range(N):
    a = int(input())
    if (a == 0):
        L.pop()
    else:
        L.append(a)

print(sum(L))
