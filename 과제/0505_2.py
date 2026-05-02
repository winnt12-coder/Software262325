N = int(input())

#3. N x N 행렬의 모든 값을 0보다 크고 (N x N x 10) 보다 작은 임의의(random) 값으로 채워주는 함수
def ran(n):
    import random
    L = []
    for i in range(n*n):
        L.append(random.randrange(1, n*n*10))
    return L

#4. 행렬 N x N을 예쁘게 출력하는 함수
def array(n, ex):
    a = 0
    for i in range(n):
        for j in range(n):
            print(f"{ex[a]:3d}", end = " ")
            a += 1
        print()

All = ran(N)
array(N, All)
print()

#2. N x N 행렬의 전치 행렬을 구하는 프로그램
a = 0
r = set()
for i in range(N):
    for j in range(N):
        if ((j*N+i), a) not in r:
            All[j*N+i], All[a] = All[a], All[j*N+i]
        r.update([(j*N+i, a), (a, j*N+i)])
        a += 1

array(N, All)
