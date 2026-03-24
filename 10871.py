N, X = map(int, input().split())
A = input().split()
for i in range(N):
    A[i] = int(A[i])

for i in range(0,N, 1):
    if(A[i] < X):
        print(A[i], end=" ")
