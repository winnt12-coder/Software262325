N, M = map(int, input().split())
n, m = set(), set()
for i in range(N):
    n.add(input())
for i in range(M):
    m.add(input())

group = n&m
g = sorted(group)
print(len(g))
for ch in g:
    print(ch)
