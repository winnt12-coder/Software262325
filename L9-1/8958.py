N = int(input())

for i in range(N):
    L = list(input())
    score = 0
    total = 0
    for ch in L:
        if (ch =='O'):
            score += 1
            total += score
        else:
            score = 0
    print(total)
    total = 0
