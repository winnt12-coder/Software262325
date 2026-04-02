N = int(input())
L = list(map(int, input().split()))
distance = 0

for i in range(N):
    for j in  range(N):
        distance += abs(L[i]-L[j])
print(distance)
