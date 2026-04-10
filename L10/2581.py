L = []
def f(n):
    n = int(n)
    r = 'yes' #변수 초기 설정
    if (n==1):
        r = 'no'
    else:
        for i in range(2, n):
            if (n%i == 0):
                r = 'no'
                break
        if r == 'yes':
            L.append(n)

M = int(input())
N = int(input())

for i in range(M, N+1):
    f(i)
if(len(L) == 0):
    print(-1)
else:
    print(sum(L))
    print(min(L))
