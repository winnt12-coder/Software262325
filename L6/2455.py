A, B = input().split()
C, D = input().split()
E, F= input().split()
G, H= input().split()

A=int(A)
B=int(B)
C=int(C)
D=int(D)
E=int(E)
F=int(F)
G=int(G)
H=int(H)

x = -A+B
y = x-C+D
z = y-E+F
r = z-G+H

print(max(x, y, z, r))
