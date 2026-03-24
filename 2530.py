A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(input())
total = A*3600 + B*60 + C + D

x = total//3600%24
y = total%3600//60
z = total%3600%60

print(x, y, z)
