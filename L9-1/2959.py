L = []
L.extend(map(int, input().split()))
L.sort(reverse=True)

print(L[1]*L[3])
