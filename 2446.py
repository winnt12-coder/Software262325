N = int(input())
i = 0

for j in range(N, 0, -1):
    print(" "*i + '*'*(2*j-1))
    i += 1
i -= 2
for a in range(2, N+1):
    print(" "*i+'*'*(2*a-1))
    i -= 1
