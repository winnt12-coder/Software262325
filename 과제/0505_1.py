N = int(input())

#3. N x N 행렬의 모든 값을 0보다 크고 (N x N x 10) 보다 작은 임의의(random) 값으로 채워주는 함수
def ran(n):
    import random
    L = []
    for i in range(n*n):
        L.append(random.randrange(1, n*n*10))
    return L

#4. 행렬 N x N을 예쁘게 출력하는 함수
def write(n, ex):
    a = 0
    for i in range(n):
        for j in range(n):
            print(f"{ex[a]:{n}d}", end = " ")
            a += 1
        print()

#1. N x N 행렬 세개 A, B, C를 곱하고 더하는, 즉, A x B + C 하는 프로그램
A = ran(N)
B = ran(N)
C = ran(N)

All = []
for i in range(N*N):
    All.append(A[i]*B[i]+C[i])

write(N, All)
