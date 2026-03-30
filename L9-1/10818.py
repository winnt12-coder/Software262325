N = int(input())
L = []
L.extend(map(int, input().split()))
L = L[:N]

print(min(L), max(L))
