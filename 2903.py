N = int(input())
d = 2
for i in range(1, N+1):
    d += 2**(i-1)

print(d**2)
