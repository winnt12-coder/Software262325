A = int(input())
B = int(input())

x = B//100
y = (B-x*100)//10
z = B-x*100-y*10

print(A*z)
print(A*y)
print(A*x)
print(A*B)
