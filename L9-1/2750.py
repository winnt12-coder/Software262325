N = int(input())
L = []

for i in range(N):
    L.append(int(input()))
L.sort()
for num in L:
    print(num)
