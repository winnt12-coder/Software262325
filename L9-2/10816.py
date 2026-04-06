N = int(input())
card = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))
c = {}

for num in card:
    if num in c:
        c[num] += 1
    else:
        c[num] = 1
for num in check:
    if num in c:
        print(c[num], end=" ")
    else:
        print(0, end=" ")
