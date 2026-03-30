N = int(input())
for i in range(N):
    L = list(map(int, input().split()))
    average = sum(L[1:])/(len(L)-1)
    mem = 0
    for num in L[1:]:
        if (num > average):
            mem += 1
    result = 100*(mem/(len(L)-1))
    print("{:.3f}%".format(result))
